# Product and technical gap baseline

Last reconciled: 2026-09-01

This ledger is derived from the current product boundary, ADRs, standards traceability, open issues, open pull requests, and exact-head GitHub evidence. It is a commercialization planning artifact, not a conformance or certification claim. Live GitHub Check state is intentionally not persisted as `queued`/`running`/`passed` here because that state changes outside the repository; merge decisions must re-fetch the current PR head and live required Checks.

## Product responsibility

`learning-interoperability-contracts` is the ContextualWisdomLab authority for versioned, provider-neutral learning interoperability contracts, schemas, profiles, mappings, conformance fixtures, and reproducible generated-client contracts. It owns no learner/application runtime state and no product database. Learning Management Platform owns enrollment/progression/completion policy; Learning Content Studio owns authored content and releases; Learning Record Store owns xAPI records and document resources; Psychometrics Commons and mathematical engines own assessment state and numerical measurement work.

## Current baseline

| Area | Evidence | Status | Commercialization gap | Next verification |
| --- | --- | --- | --- | --- |
| Repository authority | ADR 0001, README, ARCHITECTURE | Defined | Consumer dependency/versioning policy still needs executable release evidence | Merge bootstrap PR through protected `develop`, then publish an immutable versioned contract release |
| Learning event envelope | `schemas/v1/learning-event.schema.json` | Bootstrap candidate, not released/implemented evidence | `$id` still points at mutable `develop`; immutable release identity cannot be truthfully claimed before the first protected release exists | Establish an immutable release identifier before treating the schema as a supported released contract |
| JSON Schema validity | Quality workflow pins `jsonschema==4.26.0`, runs `Draft202012Validator.check_schema`, and includes a negative metaschema regression | Candidate validation; live external merge gate | A passing predecessor head cannot establish current-head evidence, and the schema still lacks an immutable release identifier | At merge time re-fetch the exact current head and require successful quality/security/SAST/review evidence |
| Timestamp contract | Range-constrained lexical pattern plus `Draft202012Validator(..., format_checker=FormatChecker())`, parser-backed calendar checks, and positive/negative edge cases | Candidate validation; live external merge gate | Repository validation covers impossible calendar dates and annotation-only `format` risk, but consumers still lack cross-language conformance proof | Re-fetch current-head quality evidence, then add consumer contract fixtures in issue #3/generated SDK work |
| Standards portfolio | `docs/doctoring/STANDARD_TRACEABILITY.md`, AGENTS.md | Adoption decisions recorded; conformance not evidenced | Adoption and implementation evidence are separated; requirement-level executable evidence is still absent for unimplemented surfaces and QTI Metadata still needs a requirement-level source before implementation | Pin exact normative requirements/test paths as each surface becomes executable; never promote adoption to conformance without exact-head evidence |
| xAPI/cmi5 interoperability | Issue #3 | Planned | No executable xAPI 2.0/profile baseline on protected `develop` | Implement issue #3 after bootstrap lands; keep cmi5/xAPI 1.0.3 compatibility distinct |
| CEFR assessment profile | PR #5 stacked on bootstrap; issue #4 | Candidate on stacked draft branch | Cannot be merge-ready until bootstrap lands and the stack is deliberately rebased/retargeted and reverified | Merge bootstrap first, restack PR #5 onto protected `develop`, rerun exact-head checks and independent review |
| Generated SDKs and cross-repository conformance | Issue #6 | Planned | No released Rust/TypeScript/Python generated contracts or consumer-driven interoperability proof | Implement after the core CEFR profile, preserving contract-only repository boundary |
| Release/package evidence | No protected released contract baseline yet | Missing | Consumers cannot pin an immutable supported contract release | Establish first release, changelog/version policy, provenance/SBOM where applicable, and immutable schema identifiers |
| Operability/security | Security/SAST workflows exist | Live external gate | No runtime service belongs here; committed CI status would become stale immediately | Keep repository read-only at runtime and require current-head supply-chain/security/generated-artifact evidence at merge/release time |

## DDD/context map

This repository is a generic interoperability subdomain. Its bounded context is **Learning Contract Authority**. Its ubiquitous language includes `contract_version`, `schema_version`, `profile_version`, `provenance_reference`, `compatibility_surface`, and `conformance_fixture`. Contract schemas and profile definitions are versioned value objects; released contract bundles are immutable release aggregates. Consumer repositories integrate through released artifacts only and must not acquire this repository's internal build tooling or cross-read another product database.

No shared-kernel database is permitted. Compatibility adapters belong in the consuming/owning runtime boundary unless the output is itself a reusable versioned interoperability mapping; such mappings may live here but remain non-authoritative for source application state.

## Release gates

A commercialization claim for a contract surface requires all of the following on the exact candidate head: schema/metaschema validation, positive and deliberately invalid fixtures, provenance/version invariants, applicable standards traceability, security/SAST checks, independent review, and an immutable release identifier. A product adoption decision is not implementation conformance, and implementation conformance is not third-party certification.

## Active gap order

1. Land bootstrap PR #1 only after its live current-head checks and unresolved review gates are satisfied.
2. Establish the first immutable release identity so versioned schema `$id` values no longer depend on mutable `develop`.
3. Deliver issue #3 executable xAPI 2.0/profile conformance while retaining the cmi5 Quartz/xAPI 1.0.3 compatibility boundary.
4. Restack and verify PR #5 for issue #4 after the bootstrap parent is protected-branch truth.
5. Implement issue #6 generated SDKs and cross-repository consumer conformance.
6. Continue replacing moving standards overview links with revision/requirement-level normative evidence as each surface becomes executable.
