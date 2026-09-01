# Changelog

## Unreleased

### Added

- Initial learning interoperability authority boundaries.
- Standards traceability baseline for xAPI, cmi5, LTI, QTI, CASE, Open Badges, CLR, and accessibility.
- Versioned learning-domain event envelope schema with an immutable semantic-version-derived logical URN.
- Repository agent development rules.
- Test-first `cwl_xapi_protocol_binding/v1` contract that keeps canonical xAPI 2.0 and cmi5 Quartz/xAPI 1.0.3 compatibility mutually exclusive without carrying statement payloads or rewriting historical records.
- Positive and deliberately invalid protocol-binding fixtures covering valid xAPI 2.0, valid cmi5 Quartz, cross-version claims, unknown surfaces, and statement-payload leakage.
- ADR 0002 documenting the protocol-binding anti-corruption boundary and current standards evidence.

### Changed

- Pinned the adopted cmi5 Quartz normative source to the official immutable Quartz release commit instead of the mutable development branch.
- Reconciled the commercialization baseline so the immutable schema identity is distinguished from the still-missing protected release artifact, and portable timestamp conformance remains explicitly blocked until consumer format-assertion fixtures are executable across supported runtimes.
- Pinned the repository quality job to `ubuntu-24.04` after the live exact-head `ubuntu-latest` job remained unassigned with no executed steps; no validation, security, review, or release gate was weakened.
- Repository Quality now executes the xAPI protocol-binding regression suite and triggers for stacked pull requests, preventing feature-branch bases from silently skipping the repository-local exact-head validation lane.
