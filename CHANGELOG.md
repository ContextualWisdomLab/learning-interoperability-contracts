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
- Rights-safe `cwl_cefr_language_assessment/v1` blueprint, task, and immutable domain-result contracts.
- CEFR positive/negative fixture gates covering standard-setting, protected content, probability mass, required-domain completeness, blueprint overall-reporting authority, and exact reporting-policy equality.
- Exact target-language profile/RLD revision or dated-snapshot requirement; standalone and compound mutable revision alias tokens fail closed.
- Distinct `cefr_aligned`, `cefr_linked`, and certification-decision evidence gates, including governed certification authority and policy references.
- Proposed ADR 0003, CEFR research doctoring, fixed standards traceability, design specification, implementation plan, and focused regression tests.

### Changed

- Pinned the adopted cmi5 Quartz normative source to the official immutable Quartz release commit instead of the mutable development branch.
- Reconciled the commercialization baseline so the immutable schema identity is distinguished from the still-missing protected release artifact, and portable timestamp conformance remains explicitly blocked until consumer format-assertion fixtures are executable across supported runtimes.
- Pinned the repository quality job to `ubuntu-24.04` after the live exact-head `ubuntu-latest` job remained unassigned with no executed steps; no validation, security, review, or release gate was weakened.
- Broadened repository Quality from only `develop`/`main` pull-request bases to every pull request so stacked feature PRs receive the same repository-local exact-head validation rather than silently skipping it.
- Repository Quality now requires PRD and TRD presence so foundational product/technical contracts cannot regress silently.
- Repository Quality fails closed if the stacked CEFR ADR advances from Proposed before protected integration.
- Rejected noncanonical leading-zero learning-event versions and added executable regressions for each semantic-version component.
- Replaced the unhashed validator install command with a binary-only, fully hash-locked dependency set.
- Added the RFC 3339 format backend and its complete transitive dependency to the hash lock so timestamp validation cannot depend on ambient runner packages.
- Pinned the JSON Schema validator to the package index's available `4.25.1` binary while retaining the complete hash-locked RFC 3339 backend closure.
