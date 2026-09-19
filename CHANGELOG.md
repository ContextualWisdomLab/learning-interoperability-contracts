# Changelog

## Unreleased

### Added

- Initial learning interoperability authority boundaries.
- Standards traceability baseline for xAPI, cmi5, LTI, QTI, CASE, Open Badges, CLR, and accessibility.
- Versioned learning-domain event envelope schema with an immutable semantic-version-derived logical URN.
- Repository agent development rules.
- Product requirements defining customer/integrator jobs, contract support gates, non-goals and release outcomes.
- Technical requirements defining the artifact-only bounded context, invariants, validation, release, security and consumer ACL requirements.
- Version-bound learning-event envelope fixtures covering two valid shapes and every current required-field, closed-object, length, semantic-version, timestamp, and data-type rejection invariant.
- A language-neutral timestamp fixture manifest preserving the repository's five valid and eleven invalid RFC 3339 lexical/calendar cases for future unchanged consumer execution.
- Test-first `cwl_xapi_protocol_binding/v1` contract that keeps canonical xAPI 2.0 and cmi5 Quartz/xAPI 1.0.3 compatibility mutually exclusive without carrying statement payloads or rewriting historical records.
- Positive and deliberately invalid protocol-binding fixtures covering valid xAPI 2.0, valid cmi5 Quartz, cross-version claims, unknown surfaces, and statement-payload leakage.
- Proposed ADR 0002 documenting the protocol-binding anti-corruption boundary and current standards evidence.
- Dependency-free Rust and TypeScript fixture consumers that execute the unchanged timestamp manifest, verify the exact case identity/distribution and reject inverted expectations.

### Changed

- Repository Quality parses exactly one anchored ADR 0001 status section and fails closed if the proposed authority advances before protected integration.
- Pinned the adopted cmi5 Quartz normative source to the official immutable Quartz release commit instead of the mutable development branch.
- Reconciled the commercialization baseline so the immutable schema identity is distinguished from the still-missing protected release artifact, and portable timestamp conformance remains explicitly blocked until consumer format-assertion fixtures are executable across supported runtimes.
- Pinned Rust 1.98.1 and Node.js 24.19.0 in repository Quality for cross-language timestamp evidence; hosted exact-head execution and protected release evidence remain required.
- Pinned the repository quality job to `ubuntu-24.04` after the live exact-head `ubuntu-latest` job remained unassigned with no executed steps; no validation, security, review, or release gate was weakened.
- Broadened repository Quality from only `develop`/`main` pull-request bases to every pull request so stacked feature PRs receive the same repository-local exact-head validation rather than silently skipping it.
- Repository Quality now requires PRD and TRD presence so foundational product/technical contracts cannot regress silently.
- Rejected noncanonical leading-zero learning-event versions and added executable regressions for each semantic-version component.
- Replaced the unhashed validator install command with a binary-only, fully hash-locked dependency set.
- Added the RFC 3339 format backend and its complete transitive dependency to the hash lock so timestamp validation cannot depend on ambient runner packages.
- Pinned the JSON Schema validator to the package index's available `4.25.1` binary while retaining the complete hash-locked RFC 3339 backend closure.
- Repository Quality executes the xAPI protocol-binding regression suite on the same exact stacked head.
- Repository Quality parses exactly one anchored xAPI ADR status declaration and fails closed if it advances from Proposed before protected integration.
