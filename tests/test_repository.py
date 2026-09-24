from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_repository


class RepositoryContractTest(unittest.TestCase):
    def test_repository_contract(self) -> None:
        self.assertEqual([], validate_repository.validate(ROOT))

    def test_use_case_capabilities_exist(self) -> None:
        manifest = validate_repository.load_json_yaml(
            ROOT / "use-cases/rhel-patching/use-case.yaml"
        )
        for capability_id in manifest["capabilities"]:
            self.assertTrue(
                (ROOT / "capabilities" / capability_id / "capability.yaml").exists(),
                capability_id,
            )

    def test_safe_demo_defaults(self) -> None:
        defaults = (
            ROOT / "use-cases/rhel-patching/demo/group_vars/all.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("demo_mode: true", defaults)
        self.assertIn("patch_execute_confirmed: false", defaults)
        self.assertIn("customer_adaptation_complete: false", defaults)


if __name__ == "__main__":
    unittest.main()
