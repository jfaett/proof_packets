#!/usr/bin/env python3
"""Validate and export the portable short-link redirect map."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    source = root / "shortlinks.yaml"
    data = json.loads(source.read_text(encoding="utf-8"))
    base_url = data["base_url"].rstrip("/")

    redirects = []
    seen = set()
    for entry in data["redirects"]:
        slug = entry["slug"].strip("/")
        if slug in seen:
            raise ValueError(f"duplicate slug: {slug}")
        seen.add(slug)
        target = root / entry["target"]
        if not target.exists():
            raise FileNotFoundError(target)
        redirects.append(
            {
                "from": f"{base_url}/go/{slug}",
                "to": entry["target"],
                "audience": entry["audience"],
            }
        )

    output_dir = root / "artifacts"
    output_dir.mkdir(exist_ok=True)
    output = output_dir / "shortlinks.json"
    output.write_text(
        json.dumps({"redirects": redirects}, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
