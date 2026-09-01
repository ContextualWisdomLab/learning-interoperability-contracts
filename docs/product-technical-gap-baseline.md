# Product and technical gap baseline

Last reconciled: 2026-09-01

This ledger is derived from the current product boundary, ADRs, standards traceability, open issues, open pull requests, and exact-head GitHub evidence. It is a commercialization planning artifact, not a conformance or certification claim.

## Product responsibility

`learning-interoperability-contracts` is the ContextualWisdomLab authority for versioned, provider-neutral learning interoperability contracts, schemas, profiles, mappings, conformance fixtures, and reproducible generated-client contracts. It owns no learner/application runtime state and no product database. Learning Management Platform owns enrollment/progression/completion policy; Learning Content Studio owns authored content and releases; Learning Record Store owns xAPI records and document resources; Psychometrics Commons and mathematical engines own assessment state and numerical measurement work.

## Current exact-head baseline

| Area | Evidence | Status | Commercialization gap | Next verification |
| --- | --- | --- | --- | --- |
| Repository authority | ADR 0001, README, ARCHITECTURE | Defined | Consumer dependency/versioning policy still needs executable release evidence | Merge bootstrap PR through protected `develop`, then publish an immutable versioned contract release |
| Learning event envelope | `schemas/v1/learning-event.schema.json` | Implemented as bootstrap schema | `$id` still points at mutable `develop`; immutable release identity cannot be truthful before the first protected release exists | After bootstrap merge, publish/tag the first immutable schema release and replace the mutable identifier in a follow-up release PR |
| JSON Schema validity | Quality workflow uses pinned `jsonschema==4.26.0` and `Draft202012Validator.check_schema` | Implemented on active bootstrap branch | Exact-head CI is still queued; no successful current-head receipt yet | Require successful exact-head quality/security/SAST checks |
| Timestamp contract | Range-constrained schema plus parser-backed positive/negative cases | Implemented on active bootstrap branch | Runtime consumers have not yet demonstrated the same acceptance/rejection behavior | Add consumer contract fixtures in issue #3 and generated SDK work |
| Standards portfolio | `docs/doctoring/STANDARD_TRACEABILITY.md` | Adoption decisions recorded; conformance not evidenced | Several standards have no executable conformance fixture and some citations remain moving overview pages | Pin normative revisions/requirements as each contract surface is implemented; never convert `Not evidenced` into conformance without executable evidence |
| xAPI/cmi5 interoperability | Issue #3 | Planned | No executable xAPI 2.0/profile baseline on protected `develop` | Implement issue #3 after bootstrap lands; keep cmi5/xAPI 1.0.3 compatibility distinct |
| CEFR assessment profile | PR #5 stacked on bootstrap; issue #4 | Implemented on stacked draft branch | Cannot be merge-ready until bootstrap lands and the stack is deliberately rebased/retargeted and reverified | Merge bootstrap first, restack PR #5 onto protected `develop`, rerun exact-head checks and independent review |
| Generated SDKs and cross-repository conformance | Issue #6 | Planned | No released Rust/TypeScript/Python generated contracts or consumer-driven interoperability proof | Implement after the core CEFR profile, preserving contract-only repository boundary |
| Release/package evidence | No protected released contract baseline yet | Missing | Consumers cannot pin an immutable supported contract release | Establish first release, changelog/version policy, provenance/SBOM where applicable, and immutable schema identifiers |
| Operability/security | Security/SAST workflows exist | Partial | Current-head evidence remains queued; no runtime service belongs here | Keep repository read-only at runtime, validate supply-chain dependencies and generated artifacts in CI |

## DDD/context map

This repository is a generic interoperability subdomain. Its bounded context is **Learning Contract Authority**. Its ubiquitous language includes `contract_version`, `schema_version`, `profile_version`, `provenance_reference`, `compatibility_surface`, and `conformance_fixture`. Contract schemas and profile definitions are versioned value objects; released contract bundles are immutable release aggregates. Consumer repositories integrate through released artifacts only and must not acquire this repository's internal build tooling or cross-read another product database.

No shared-kernel database is permitted. Compatibility adapters belong in the consuming/owning runtime boundary unless the output is itself a reusable versioned interoperability mapping; such mappings may live here but remain non-authoritative for source application state.

## Release gates

A commercialization claim for a contract surface requires all of the following on the exact candidate head: schema/metaschema validation, positive and deliberately invalid fixtures, provenance/version invariants, applicable standards traceability, security/SAST checks, independent review, and an immutable release identifier. A product adoption decision is not implementation conformance, and implementation conformance is not third-party certification.

## Active gap order

1. Land bootstrap PR #1 only after its exact-head checks and unresolved review gates are satisfied.
2. Establish the first immutable release identity so versioned schema `$id` values no longer depend on mutable `develop`.
3. Deliver issue #3 executable xAPI 2.0/profile conformance while retaining the cmi5 Quartz/xAPI 1.0.3 compatibility boundary.
4. Restack and verify PR #5 for issue #4 after the bootstrap parent is protected-branch truth.
5. Implement issue #6 generated SDKs and cross-repository consumer conformance.
6. Continue replacing moving standards overview links with revision/requirement-level normative evidence as each surface becomes executable.
