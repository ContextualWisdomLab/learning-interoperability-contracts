"""Validate the versioned CEFR interoperability profile with the Python standard library."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Callable

PROFILE_ROOT = Path("profiles/cwl_cefr_language_assessment/v1")
SCHEMA_ROOT = PROFILE_ROOT / "schemas"
VALID_ROOT = PROFILE_ROOT / "conformance" / "valid"
INVALID_ROOT = PROFILE_ROOT / "conformance" / "invalid"
PUBLISHED_PREFIX = (
    "https://raw.githubusercontent.com/ContextualWisdomLab/"
    "learning-interoperability-contracts/develop/"
    "profiles/cwl_cefr_language_assessment/v1/schemas/"
)
FORBIDDEN_KEYS = {
    "descriptor_text",
    "descriptor_prose",
    "can_do_text",
    "task_content",
    "raw_response",
    "response_text",
    "audio_bytes",
    "provider_payload",
    "model_output",
    "personal_data",
}


def load_json(path: Path) -> dict[str, Any]:
    """Load one JSON object and reject non-object roots."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def reject_forbidden_payload(value: Any, location: str = "$") -> None:
    """Reject protected prose, content, response, provider, and personal-data fields."""
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in FORBIDDEN_KEYS:
                raise ValueError(f"forbidden payload field {key!r} at {location}")
            reject_forbidden_payload(nested, f"{location}.{key}")
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            reject_forbidden_payload(nested, f"{location}[{index}]")


def require_reference(value: Any, field: str) -> None:
    """Require one exact, nonnumeric, control-free opaque reference."""
    if not isinstance(value, str) or len(value) < 3 or value != value.strip() or value.isnumeric():
        raise ValueError(f"{field} must be an exact nonnumeric opaque reference")
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise ValueError(f"{field} contains an ASCII control")


def validate_probability_set(value: Any, field: str) -> None:
    """Require finite probabilities in [0, 1] whose mass equals one."""
    if not isinstance(value, dict) or len(value) < 2:
        raise ValueError(f"{field} must contain at least two level probabilities")
    numbers = list(value.values())
    if any(
        not isinstance(item, (int, float))
        or isinstance(item, bool)
        or not math.isfinite(item)
        or item < 0
        or item > 1
        for item in numbers
    ):
        raise ValueError(f"{field} contains an invalid probability")
    if not math.isclose(sum(numbers), 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise ValueError(f"{field} probability mass must equal one")


def validate_blueprint(value: dict[str, Any]) -> None:
    """Validate scientific and claim gates for an assessment blueprint fixture."""
    reject_forbidden_payload(value)
    if value.get("contract_version") != "cwl_cefr_language_assessment/assessment_blueprint/v1":
        raise ValueError("wrong blueprint contract version")
    for field in (
        "blueprint_reference",
        "framework_version_reference",
        "language_reference_level_description_reference",
        "instrument_release_reference",
        "scoring_profile_reference",
        "cut_score_revision_reference",
    ):
        require_reference(value.get(field), field)
    if value.get("descriptor_source_policy_code") != "reference_only_no_descriptor_copy":
        raise ValueError("descriptor source policy must prohibit copies")
    required = value.get("required_domain_codes")
    optional = value.get("optional_domain_codes", [])
    if not isinstance(required, list) or not required or len(required) != len(set(required)):
        raise ValueError("required domains must be nonempty and unique")
    if not isinstance(optional, list) or len(optional) != len(set(optional)) or set(required) & set(optional):
        raise ValueError("required and optional domains must be disjoint")
    if value.get("reporting_scope_code") == "overall_and_profile" and not value.get(
        "overall_reporting_policy_reference"
    ):
        raise ValueError("overall reporting needs a policy reference")
    if (
        value.get("decision_stakes_code") == "high"
        or value.get("assessment_purpose_code") == "certification"
    ) and not value.get("standard_setting_study_reference"):
        raise ValueError("high-stakes/certification blueprint needs standard setting")


def validate_task(value: dict[str, Any]) -> None:
    """Validate a reference-only CEFR task fixture."""
    reject_forbidden_payload(value)
    if value.get("contract_version") != "cwl_cefr_language_assessment/task_specification/v1":
        raise ValueError("wrong task contract version")
    for field in (
        "task_reference",
        "task_revision_reference",
        "assessment_blueprint_reference",
        "source_content_release_reference",
        "accessibility_profile_reference",
        "rights_reference",
        "linguistic_demand_reference",
        "cognitive_demand_reference",
        "evidence_model_reference",
    ):
        require_reference(value.get(field), field)
    descriptors = value.get("descriptor_references")
    if not isinstance(descriptors, list) or not descriptors or len(descriptors) != len(set(descriptors)):
        raise ValueError("descriptor references must be nonempty and unique")
    for descriptor in descriptors:
        require_reference(descriptor, "descriptor_reference")
    if value.get("descriptor_source_policy_code") != "reference_only_no_descriptor_copy":
        raise ValueError("descriptor source policy must prohibit copies")
    if value.get("response_mode_code") != "selected_response" and not value.get("rubric_revision_reference"):
        raise ValueError("constructed response needs a rubric revision")
    if value.get("communication_mode_code") == "interaction" and not value.get(
        "interaction_demand_reference"
    ):
        raise ValueError("interaction task needs interaction demand evidence")
    if value.get("communication_mode_code") == "mediation" and not value.get("mediation_demand_reference"):
        raise ValueError("mediation task needs mediation demand evidence")
    digest = value.get("task_content_digest")
    if (
        not isinstance(digest, str)
        or len(digest) != 71
        or not digest.startswith("sha256:")
        or any(character not in "0123456789abcdef" for character in digest[7:])
    ):
        raise ValueError("task digest must be canonical lowercase sha256")


def validate_result(value: dict[str, Any]) -> None:
    """Validate domain uncertainty, linking claims, and overall-reporting gates."""
    reject_forbidden_payload(value)
    if value.get("contract_version") != "cwl_cefr_language_assessment/result_snapshot/v1":
        raise ValueError("wrong result contract version")
    for field in (
        "result_reference",
        "participant_reference",
        "assessment_session_reference",
        "instrument_release_reference",
        "assessment_blueprint_reference",
        "scoring_profile_reference",
        "cut_score_revision_reference",
    ):
        require_reference(value.get(field), field)
    if value.get("claim_status_code") in {"cefr_linked", "certification_decision"}:
        require_reference(value.get("standard_setting_study_reference"), "standard_setting_study_reference")
        require_reference(value.get("linking_validation_reference"), "linking_validation_reference")
    domains = value.get("domain_results")
    if not isinstance(domains, list) or not domains:
        raise ValueError("domain results must be nonempty")
    codes = [item.get("domain_code") for item in domains]
    if len(codes) != len(set(codes)):
        raise ValueError("domain identities must be unique")
    measured_fields = {
        "reported_level_code",
        "level_probabilities",
        "credible_level_set",
        "standard_error",
        "descriptor_coverage_references",
    }
    for item in domains:
        if item.get("measurement_status_code") == "measured":
            missing = sorted(field for field in measured_fields if field not in item)
            if missing:
                raise ValueError(f"measured domain is missing {missing}")
            validate_probability_set(item["level_probabilities"], f"{item.get('domain_code')}.level_probabilities")
            if item["reported_level_code"] not in item["level_probabilities"]:
                raise ValueError("reported domain level must have probability evidence")
            if item["reported_level_code"] not in item["credible_level_set"]:
                raise ValueError("reported domain level must be in credible set")
        elif measured_fields & item.keys():
            raise ValueError("unmeasured domain must not carry an invented score")
    overall = value.get("overall_result")
    if not isinstance(overall, dict):
        raise ValueError("overall result is required")
    if overall.get("reporting_status_code") == "reported":
        if overall.get("required_domain_completeness_code") != "complete":
            raise ValueError("overall result requires complete required domains")
        require_reference(overall.get("reporting_policy_reference"), "reporting_policy_reference")
        validate_probability_set(overall.get("level_probabilities"), "overall.level_probabilities")
        if overall.get("reported_level_code") not in overall.get("level_probabilities", {}):
            raise ValueError("reported overall level must have probability evidence")
        if overall.get("reported_level_code") not in overall.get("credible_level_set", []):
            raise ValueError("reported overall level must be in credible set")
    elif any(
        field in overall
        for field in ("reported_level_code", "level_probabilities", "credible_level_set", "reporting_policy_reference")
    ):
        raise ValueError("not-reported overall result must not carry an invented score")


def validate_schema_metadata() -> None:
    """Validate exact schema draft, version, and published identifiers."""
    schemas = [load_json(path) for path in sorted(SCHEMA_ROOT.glob("*.json"))]
    if len(schemas) != 4:
        raise ValueError("the CEFR v1 profile must publish exactly four schemas")
    for schema in schemas:
        name = Path(schema["$id"]).name
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise ValueError(f"{name} must use JSON Schema Draft 2020-12")
        if schema.get("x-cwl-schema-version") != "1.0.0":
            raise ValueError(f"{name} must declare schema version 1.0.0")
        if schema.get("$id") != PUBLISHED_PREFIX + name:
            raise ValueError(f"{name} has the wrong published $id")


def main() -> None:
    """Run profile presence, positive-fixture, and negative-fixture validation."""
    required = [
        PROFILE_ROOT / "README.md",
        Path("docs/adr/0002-cefr-language-assessment-profile.md"),
        Path("docs/doctoring/CEFR_LANGUAGE_ASSESSMENT.md"),
        Path("docs/superpowers/specs/2026-08-27-cefr-language-assessment-profile-design.md"),
        Path("docs/superpowers/plans/2026-08-27-cefr-language-assessment-profile.md"),
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ValueError(f"missing CEFR profile files: {missing}")
    validate_schema_metadata()
    positive: dict[str, Callable[[dict[str, Any]], None]] = {
        "assessment-blueprint.json": validate_blueprint,
        "task-specification.json": validate_task,
        "cefr-result-snapshot-profile-only.json": validate_result,
        "cefr-result-snapshot-linked-overall.json": validate_result,
    }
    for filename, validator in positive.items():
        validator(load_json(VALID_ROOT / filename))
    negative: dict[str, Callable[[dict[str, Any]], None]] = {
        "high-stakes-blueprint-without-standard-setting.json": validate_blueprint,
        "task-with-copied-descriptor-text.json": validate_task,
        "overall-result-with-incomplete-required-domain.json": validate_result,
        "result-with-nonunit-probability-mass.json": validate_result,
    }
    for filename, validator in negative.items():
        try:
            validator(load_json(INVALID_ROOT / filename))
        except ValueError:
            continue
        raise ValueError(f"negative CEFR fixture unexpectedly passed: {filename}")
    print("CEFR language-assessment profile validation passed")


if __name__ == "__main__":
    main()
