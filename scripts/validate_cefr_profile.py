"""Validate CEFR contracts with Draft 2020-12 and cross-artifact semantics."""

from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource

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
SCHEMA_FILENAMES = {
    "blueprint": "assessment-blueprint.schema.json",
    "task": "task-specification.schema.json",
    "result": "cefr-result-snapshot.schema.json",
}


def load_json(path: Path) -> dict[str, Any]:
    """Load one JSON object and reject non-object roots."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


@lru_cache(maxsize=1)
def load_schemas() -> dict[str, dict[str, Any]]:
    """Load every committed CEFR schema by filename exactly once per process."""
    return {
        path.name: load_json(path)
        for path in sorted(SCHEMA_ROOT.glob("*.json"))
    }


@lru_cache(maxsize=1)
def build_schema_registry() -> Registry:
    """Build an offline registry for absolute and relative CEFR schema references."""
    resources = []
    for schema in load_schemas().values():
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str):
            raise ValueError("every CEFR schema must declare a string $id")
        resources.append((schema_id, Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validate_against_schema(value: dict[str, Any], schema_filename: str) -> None:
    """Apply the committed Draft 2020-12 schema before semantic validation."""
    try:
        schema = load_schemas()[schema_filename]
    except KeyError as error:
        raise ValueError(f"unknown CEFR schema {schema_filename!r}") from error
    validator = Draft202012Validator(schema, registry=build_schema_registry())
    errors = sorted(validator.iter_errors(value), key=lambda error: error.json_path)
    if errors:
        first = errors[0]
        raise ValueError(
            f"{schema_filename} JSON Schema violation at {first.json_path}: "
            f"{first.message}"
        )


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
    if (
        not isinstance(value, str)
        or len(value) < 3
        or value != value.strip()
        or value.isnumeric()
    ):
        raise ValueError(f"{field} must be an exact nonnumeric opaque reference")
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise ValueError(f"{field} contains an ASCII control")


def require_immutable_revision(value: Any, field: str) -> None:
    """Reject mutable revision aliases while permitting publisher or snapshot IDs."""
    require_reference(value, field)
    if str(value).strip().lower() in {"latest", "current", "head", "main"}:
        raise ValueError(f"{field} must not use a mutable revision alias")


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
    """Validate structural, scientific, rights, and claim gates for a blueprint."""
    validate_against_schema(value, SCHEMA_FILENAMES["blueprint"])
    reject_forbidden_payload(value)
    for field in (
        "blueprint_reference",
        "framework_version_reference",
        "language_reference_level_description_reference",
        "instrument_release_reference",
        "scoring_profile_reference",
        "cut_score_revision_reference",
    ):
        require_reference(value.get(field), field)
    require_immutable_revision(
        value.get("language_reference_level_description_revision"),
        "language_reference_level_description_revision",
    )
    if value.get("descriptor_source_policy_code") != "reference_only_no_descriptor_copy":
        raise ValueError("descriptor source policy must prohibit copies")
    required = value.get("required_domain_codes")
    optional = value.get("optional_domain_codes", [])
    if not isinstance(required, list) or not required or len(required) != len(set(required)):
        raise ValueError("required domains must be nonempty and unique")
    if (
        not isinstance(optional, list)
        or len(optional) != len(set(optional))
        or set(required) & set(optional)
    ):
        raise ValueError("required and optional domains must be disjoint")
    if value.get("reporting_scope_code") == "overall_and_profile":
        require_reference(
            value.get("overall_reporting_policy_reference"),
            "overall_reporting_policy_reference",
        )
    if (
        value.get("decision_stakes_code") == "high"
        or value.get("assessment_purpose_code") == "certification"
    ):
        require_reference(
            value.get("standard_setting_study_reference"),
            "standard_setting_study_reference",
        )


def validate_task(value: dict[str, Any]) -> None:
    """Validate a closed, reference-only CEFR task document."""
    validate_against_schema(value, SCHEMA_FILENAMES["task"])
    reject_forbidden_payload(value)
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
    if value.get("response_mode_code") != "selected_response":
        require_reference(value.get("rubric_revision_reference"), "rubric_revision_reference")
    if value.get("communication_mode_code") == "interaction":
        require_reference(
            value.get("interaction_demand_reference"),
            "interaction_demand_reference",
        )
    if value.get("communication_mode_code") == "mediation":
        require_reference(
            value.get("mediation_demand_reference"),
            "mediation_demand_reference",
        )
    digest = value.get("task_content_digest")
    if (
        not isinstance(digest, str)
        or len(digest) != 71
        or not digest.startswith("sha256:")
        or any(character not in "0123456789abcdef" for character in digest[7:])
    ):
        raise ValueError("task digest must be canonical lowercase sha256")


def load_blueprint_registry() -> dict[str, dict[str, Any]]:
    """Load and validate every positive blueprint by its immutable reference."""
    registry: dict[str, dict[str, Any]] = {}
    for path in sorted(VALID_ROOT.glob("assessment-blueprint*.json")):
        blueprint = load_json(path)
        validate_blueprint(blueprint)
        reference = blueprint["blueprint_reference"]
        if reference in registry:
            raise ValueError(f"duplicate blueprint reference {reference!r}")
        registry[reference] = blueprint
    if not registry:
        raise ValueError("at least one positive assessment blueprint is required")
    return registry


def resolve_blueprint(reference: Any) -> dict[str, Any]:
    """Resolve one result's exact blueprint or fail closed."""
    require_reference(reference, "assessment_blueprint_reference")
    try:
        return load_blueprint_registry()[str(reference)]
    except KeyError as error:
        raise ValueError(f"unknown assessment blueprint reference {reference!r}") from error


def validate_result(value: dict[str, Any]) -> None:
    """Validate structure, uncertainty, claims, and blueprint reporting authority."""
    validate_against_schema(value, SCHEMA_FILENAMES["result"])
    reject_forbidden_payload(value)
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
    blueprint = resolve_blueprint(value["assessment_blueprint_reference"])
    for result_field, blueprint_field in (
        ("instrument_release_reference", "instrument_release_reference"),
        ("scoring_profile_reference", "scoring_profile_reference"),
        ("cut_score_revision_reference", "cut_score_revision_reference"),
        ("target_language", "target_language"),
    ):
        if value.get(result_field) != blueprint.get(blueprint_field):
            raise ValueError(
                f"result {result_field} must equal its immutable blueprint value"
            )
    if value.get("claim_status_code") in {"cefr_linked", "certification_decision"}:
        require_reference(
            value.get("standard_setting_study_reference"),
            "standard_setting_study_reference",
        )
        require_reference(
            value.get("linking_validation_reference"),
            "linking_validation_reference",
        )
    if value.get("claim_status_code") == "certification_decision":
        require_reference(
            value.get("certification_authority_reference"),
            "certification_authority_reference",
        )
        require_reference(
            value.get("certification_policy_reference"),
            "certification_policy_reference",
        )
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
    measured_domains: set[str] = set()
    for item in domains:
        if item.get("measurement_status_code") == "measured":
            measured_domains.add(str(item.get("domain_code")))
            missing = sorted(field for field in measured_fields if field not in item)
            if missing:
                raise ValueError(f"measured domain is missing {missing}")
            validate_probability_set(
                item["level_probabilities"],
                f"{item.get('domain_code')}.level_probabilities",
            )
            if item["reported_level_code"] not in item["level_probabilities"]:
                raise ValueError("reported domain level must have probability evidence")
            if item["reported_level_code"] not in item["credible_level_set"]:
                raise ValueError("reported domain level must be in credible set")
        elif measured_fields & item.keys():
            raise ValueError("unmeasured domain must not carry an invented score")
    required_domains = set(blueprint["required_domain_codes"])
    missing_required_domains = sorted(required_domains - measured_domains)
    overall = value.get("overall_result")
    if not isinstance(overall, dict):
        raise ValueError("overall result is required")
    declared_completeness = overall.get("required_domain_completeness_code")
    actual_completeness = "incomplete" if missing_required_domains else "complete"
    if declared_completeness != actual_completeness:
        raise ValueError(
            "overall required-domain completeness disagrees with the immutable blueprint"
        )
    if overall.get("reporting_status_code") == "reported":
        if blueprint.get("reporting_scope_code") != "overall_and_profile":
            raise ValueError("assessment blueprint does not authorize overall reporting")
        if missing_required_domains:
            raise ValueError(
                "overall result cannot be reported with unmeasured required domains"
            )
        expected_policy = blueprint.get("overall_reporting_policy_reference")
        if overall.get("reporting_policy_reference") != expected_policy:
            raise ValueError(
                "overall reporting policy must equal the immutable blueprint policy"
            )
        validate_probability_set(
            overall.get("level_probabilities"),
            "overall.level_probabilities",
        )
        if overall.get("reported_level_code") not in overall.get("level_probabilities", {}):
            raise ValueError("reported overall level must have probability evidence")
        if overall.get("reported_level_code") not in overall.get("credible_level_set", []):
            raise ValueError("reported overall level must be in credible set")
    elif any(
        field in overall
        for field in (
            "reported_level_code",
            "level_probabilities",
            "credible_level_set",
            "reporting_policy_reference",
        )
    ):
        raise ValueError("not-reported overall result must not carry an invented score")


def validate_schema_metadata() -> None:
    """Validate exact draft, version, identifiers, and schema metaschema syntax."""
    schemas = load_schemas()
    if len(schemas) != 4:
        raise ValueError("the CEFR v1 profile must publish exactly four schemas")
    for name, schema in schemas.items():
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise ValueError(f"{name} must use JSON Schema Draft 2020-12")
        if schema.get("x-cwl-schema-version") != "1.0.0":
            raise ValueError(f"{name} must declare schema version 1.0.0")
        if schema.get("$id") != PUBLISHED_PREFIX + name:
            raise ValueError(f"{name} has the wrong published $id")
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as error:
            raise ValueError(f"{name} is not a valid Draft 2020-12 schema") from error
    build_schema_registry()


def main() -> None:
    """Run presence, Draft 2020-12, positive, and negative fixture validation."""
    required = [
        PROFILE_ROOT / "README.md",
        Path("docs/adr/0002-cefr-language-assessment-profile.md"),
        Path("docs/doctoring/CEFR_LANGUAGE_ASSESSMENT.md"),
        Path("docs/superpowers/specs/2026-08-27-cefr-language-assessment-profile-design.md"),
        Path("docs/superpowers/plans/2026-08-27-cefr-language-assessment-profile.md"),
        Path("requirements-contracts-ci-hashes.txt"),
        Path("tests/test_validate_cefr_profile.py"),
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ValueError(f"missing CEFR profile files: {missing}")
    validate_schema_metadata()
    for path in sorted(VALID_ROOT.glob("assessment-blueprint*.json")):
        validate_blueprint(load_json(path))
    for path in sorted(VALID_ROOT.glob("task-specification*.json")):
        validate_task(load_json(path))
    for path in sorted(VALID_ROOT.glob("cefr-result-snapshot*.json")):
        validate_result(load_json(path))
    negative: dict[str, Callable[[dict[str, Any]], None]] = {
        "high-stakes-blueprint-without-standard-setting.json": validate_blueprint,
        "task-with-copied-descriptor-text.json": validate_task,
        "overall-result-with-incomplete-required-domain.json": validate_result,
        "overall-result-with-profile-only-blueprint.json": validate_result,
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
