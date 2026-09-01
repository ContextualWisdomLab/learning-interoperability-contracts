"""Regression contract for the CWL xAPI/cmi5 protocol binding surface."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "profiles" / "cwl_xapi_protocol_binding" / "v1" / "protocol-binding.schema.json"
VALID_FIXTURES = ROOT / "fixtures" / "xapi_protocol_binding" / "valid"
INVALID_FIXTURES = ROOT / "fixtures" / "xapi_protocol_binding" / "invalid"


class XapiProtocolBindingContractTests(unittest.TestCase):
    """Require explicit, non-translating xAPI 2.0 and cmi5 Quartz bindings."""

    @classmethod
    def setUpClass(cls) -> None:
        """Load the candidate schema and prove it is valid Draft 2020-12."""
        with SCHEMA_PATH.open(encoding="utf-8") as handle:
            cls.schema = json.load(handle)
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def test_schema_identity_is_versioned_and_provider_neutral(self) -> None:
        """Pin the shared contract identity without claiming a product runtime boundary."""
        self.assertEqual(
            self.schema["$id"],
            "urn:contextualwisdomlab:learning-interoperability-contracts:xapi-protocol-binding:1.0.0",
        )
        self.assertEqual(self.schema["x-cwl-schema-version"], "1.0.0")
        self.assertEqual(self.schema["properties"]["contract_id"]["const"], "cwl_xapi_protocol_binding/v1")

    def test_valid_bindings_are_accepted(self) -> None:
        """Accept canonical xAPI 2.0 and explicit Quartz/xAPI 1.0.3 compatibility bindings."""
        paths = sorted(VALID_FIXTURES.glob("*.json"))
        self.assertGreaterEqual(len(paths), 2)
        for path in paths:
            with self.subTest(path=path.name):
                with path.open(encoding="utf-8") as handle:
                    payload = json.load(handle)
                self.assertEqual(list(self.validator.iter_errors(payload)), [])

    def test_invalid_cross_version_bindings_fail_closed(self) -> None:
        """Reject version crossover, unknown surfaces, and permissive extra fields."""
        paths = sorted(INVALID_FIXTURES.glob("*.json"))
        self.assertGreaterEqual(len(paths), 4)
        for path in paths:
            with self.subTest(path=path.name):
                with path.open(encoding="utf-8") as handle:
                    payload = json.load(handle)
                self.assertNotEqual(list(self.validator.iter_errors(payload)), [])

    def test_no_statement_payload_is_owned_by_the_binding_contract(self) -> None:
        """Keep statement/runtime truth outside this protocol-selection value object."""
        self.assertNotIn("statement", self.schema["properties"])
        self.assertFalse(self.schema["additionalProperties"])


if __name__ == "__main__":
    unittest.main()
