# Changelog

## Unreleased

### Added

- Initial learning interoperability authority boundaries.
- Standards traceability baseline for xAPI, cmi5, LTI, QTI, CASE, Open Badges, CLR, and accessibility.
- Versioned learning-domain event envelope schema with an immutable semantic-version-derived logical URN.
- Repository agent development rules.
- Product requirements defining customer/integrator jobs, contract support gates, non-goals and release outcomes.
- Technical requirements defining the artifact-only bounded context, invariants, validation, release, security and consumer ACL requirements.

### Changed

- Pinned the adopted cmi5 Quartz normative source to the official immutable Quartz release commit instead of the mutable development branch.
- Reconciled the commercialization baseline so the immutable schema identity is distinguished from the still-missing protected release artifact, and portable timestamp conformance remains explicitly blocked until consumer format-assertion fixtures are executable across supported runtimes.
- Pinned the repository quality job to `ubuntu-24.04` after the live exact-head `ubuntu-latest` job remained unassigned with no executed steps; no validation, security, review, or release gate was weakened.
- Broadened repository Quality from only `develop`/`main` pull-request bases to every pull request so stacked feature PRs receive the same repository-local exact-head validation rather than silently skipping it.
- Repository Quality now requires PRD and TRD presence so foundational product/technical contracts cannot regress silently.
