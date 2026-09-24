#!/usr/bin/env python3
"""Validate Proof Pack structure, references, safety markers, and deep links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT_REQUIRED = [
    "README.md",
    "VERSION",
    "catalog.yaml",
    "shortlinks.yaml",
    "docs",
    "practices",
    "templates",
    "governance",
    "capabilities",
    "use-cases",
]

PACK_REQUIRED = [
    "README.md",
    "use-case.yaml",
    "01-seller-briefing.md",
    "02-discovery-guide.md",
    "current-state/illustrative-sop.md",
    "current-state/process-map.md",
    "current-state/baseline-worksheet.md",
    "04-decomposition.md",
    "05-solution-pattern.md",
    "demo/setup.md",
    "demo/talk-track.md",
    "demo/expected-results.md",
    "demo/reset-demo.md",
    "demo/playbooks/rhel_patch_window.yml",
    "06-measurement-and-proof.md",
    "07-pov-success-criteria.md",
    "08-failure-and-recovery.md",
    "09-expansion-paths.md",
    "10-evidence-and-sources.md",
    "OWNERS.md",
    "CHANGELOG.md",
    "tests/scenarios.md",
]

CAPABILITY_REQUIRED = [
    "README.md",
    "capability.yaml",
    "defaults/main.yml",
    "tasks/main.yml",
    "tests/contract.yml",
]

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def load_json_yaml(path: Path) -> dict:
    """Manifests use the JSON subset of YAML for dependency-free validation."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: invalid JSON-compatible YAML: {exc}") from exc


def check_required(root: Path, items: list[str], errors: list[str]) -> None:
    for item in items:
        if not (root / item).exists():
            errors.append(f"missing required path: {root / item}")


def check_markdown_links(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
            ):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken relative link in {path}: {raw_target}")


def check_manifests(root: Path, errors: list[str]) -> None:
    try:
        catalog = load_json_yaml(root / "catalog.yaml")
        shortlinks = load_json_yaml(root / "shortlinks.yaml")
        manifest = load_json_yaml(root / "use-cases/rhel-patching/use-case.yaml")
    except ValueError as exc:
        errors.append(str(exc))
        return

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER_PATTERN.match(version):
        errors.append(f"VERSION is not semantic: {version}")
    if catalog.get("repository_version") != version:
        errors.append("catalog repository_version does not match VERSION")

    required_manifest_keys = {
        "schema_version",
        "id",
        "title",
        "summary",
        "version",
        "status",
        "maturity",
        "illustrative",
        "outcome",
        "actors",
        "systems",
        "metrics",
        "capabilities",
        "evidence",
        "owners",
        "validation",
        "deep_link_slug",
    }
    missing = sorted(required_manifest_keys - set(manifest))
    if missing:
        errors.append(f"use-case manifest missing keys: {', '.join(missing)}")

    catalog_capabilities = {
        item["id"] for item in catalog.get("capabilities", []) if "id" in item
    }
    manifest_capabilities = set(manifest.get("capabilities", []))
    if missing_caps := sorted(manifest_capabilities - catalog_capabilities):
        errors.append(f"manifest references uncataloged capabilities: {missing_caps}")

    actual_caps = {
        path.parent.name for path in (root / "capabilities").glob("*/capability.yaml")
    }
    if catalog_capabilities != actual_caps:
        errors.append(
            "catalog capability set differs from capability directories: "
            f"catalog={sorted(catalog_capabilities)}, actual={sorted(actual_caps)}"
        )

    slugs: set[str] = set()
    for redirect in shortlinks.get("redirects", []):
        slug = redirect.get("slug")
        target = redirect.get("target")
        if not slug or slug in slugs:
            errors.append(f"missing or duplicate short-link slug: {slug}")
        slugs.add(slug)
        if not target or not (root / target).exists():
            errors.append(f"short-link target does not exist: {target}")

    for capability_file in (root / "capabilities").glob("*/capability.yaml"):
        try:
            capability = load_json_yaml(capability_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        expected_id = capability_file.parent.name
        if capability.get("id") != expected_id:
            errors.append(
                f"{capability_file}: id {capability.get('id')} must match {expected_id}"
            )
        if not SEMVER_PATTERN.match(str(capability.get("version", ""))):
            errors.append(f"{capability_file}: version must be semantic")
        for key in (
            "owner_role",
            "inputs",
            "outputs",
            "failures",
            "evidence",
            "consumers",
            "support_boundary",
        ):
            if key not in capability:
                errors.append(f"{capability_file}: missing {key}")


def check_safety_and_labels(root: Path, errors: list[str]) -> None:
    pack = root / "use-cases/rhel-patching"
    combined = "\n".join(
        path.read_text(encoding="utf-8") for path in pack.rglob("*.md")
    )
    for label in ("ILLUSTRATIVE", "CUSTOMER INPUT REQUIRED"):
        if label not in combined:
            errors.append(f"RHEL pack does not use required label: {label}")

    playbook = (pack / "demo/playbooks/rhel_patch_window.yml").read_text(
        encoding="utf-8"
    )
    for gate in (
        "customer_adaptation_complete",
        "patch_execute_confirmed",
        "approval_authoritative",
    ):
        if gate not in playbook:
            errors.append(f"live demo safety gate missing: {gate}")

    forbidden = {
        "validate_certs:" + " false": "TLS validation disabled",
        "host_key_checking" + " = False": "SSH host-key checking disabled",
    }
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for token, reason in forbidden.items():
            if token in text:
                errors.append(f"{path}: {reason}")

    bundled_pdfs = list(root.rglob("*.pdf"))
    if bundled_pdfs:
        errors.append(f"source PDFs must not be bundled: {bundled_pdfs}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    check_required(root, ROOT_REQUIRED, errors)

    pack = root / "use-cases/rhel-patching"
    check_required(pack, PACK_REQUIRED, errors)

    for capability in (root / "capabilities").iterdir():
        if capability.is_dir():
            check_required(capability, CAPABILITY_REQUIRED, errors)

    check_manifests(root, errors)
    check_markdown_links(root, errors)
    check_safety_and_labels(root, errors)
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print(f"FAIL: {len(errors)} repository validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: repository structure, manifests, links, labels, and safety checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
