"""Regression tests for CEFR schema and cross-artifact authority validation."""

from __future__ import annotations

import copy
import unittest

from scripts import validate_cefr_profile as validator


class CefrProfileValidationTests(unittest.TestCase):
    """Lock structural schema and immutable blueprint authorization behavior."""

    def test_blueprint_missing_schema_required_target_language_is_rejected(self) -> None:
        """Custom checks cannot admit a blueprint rejected by Draft 2020-12."""
        blueprint = validator.load_json(
            validator.VALID_ROOT / "assessment-blueprint.json"
        )
        del blueprint["target_language"]

        with self.assertRaises(ValueError):
            validator.validate_blueprint(blueprint)

    def test_blueprint_unknown_field_is_rejected(self) -> None:
        """Closed schemas reject unknown payload fields before semantic checks."""
        blueprint = validator.load_json(
            validator.VALID_ROOT / "assessment-blueprint.json"
        )
        blueprint["unexpected_contract_field"] = "not-permitted"

        with self.assertRaises(ValueError):
            validator.validate_blueprint(blueprint)

    def test_overall_result_is_rejected_by_profile_only_blueprint(self) -> None:
        """A snapshot cannot self-authorize overall reporting."""
        profile_blueprint = validator.load_json(
            validator.VALID_ROOT / "assessment-blueprint.json"
        )
        result = validator.load_json(
            validator.VALID_ROOT / "cefr-result-snapshot-linked-overall.json"
        )
        result["assessment_blueprint_reference"] = profile_blueprint[
            "blueprint_reference"
        ]

        with self.assertRaises(ValueError):
            validator.validate_result(result)

    def test_overall_result_requires_every_blueprint_domain_measured(self) -> None:
        """Snapshot completeness must match the immutable blueprint domain set."""
        overall_blueprint = validator.load_json(
            validator.VALID_ROOT / "assessment-blueprint-overall.json"
        )
        result = validator.load_json(
            validator.VALID_ROOT / "cefr-result-snapshot-linked-overall.json"
        )
        result["assessment_blueprint_reference"] = overall_blueprint[
            "blueprint_reference"
        ]
        result["domain_results"] = [
            domain
            for domain in result["domain_results"]
            if domain["domain_code"] != "spoken_production"
        ]

        with self.assertRaises(ValueError):
            validator.validate_result(result)

    def test_overall_policy_must_equal_blueprint_policy(self) -> None:
        """A result cannot substitute its own overall-reporting policy."""
        overall_blueprint = validator.load_json(
            validator.VALID_ROOT / "assessment-blueprint-overall.json"
        )
        result = copy.deepcopy(
            validator.load_json(
                validator.VALID_ROOT / "cefr-result-snapshot-linked-overall.json"
            )
        )
        result["assessment_blueprint_reference"] = overall_blueprint[
            "blueprint_reference"
        ]
        result["overall_result"][
            "reporting_policy_reference"
        ] = "different_overall_reporting_policy"

        with self.assertRaises(ValueError):
            validator.validate_result(result)


if __name__ == "__main__":
    unittest.main()
