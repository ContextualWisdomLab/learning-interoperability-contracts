# Product and technical gap baseline

Last reconciled: 2026-09-01

This ledger is derived from the current product boundary, ADRs, standards traceability, open issues, open pull requests, and exact-head GitHub evidence. It is a commercialization planning artifact, not a conformance or certification claim. Live GitHub Check state is intentionally not persisted as `queued`/`running`/`passed` here because that state changes outside the repository; merge decisions must re-fetch the current PR head and live required Checks.

## Product responsibility

`learning-interoperability-contracts` is the ContextualWisdomLab authority for versioned, provider-neutral learning interoperability contracts, schemas, profiles, mappings, conformance fixtures, and reproducible generated-client contracts. It owns no learner/application runtime state and no product database. Learning Management Platform owns enrollment/progression/completion policy; Learning Content Studio owns authored content and releases; Learning Record Store owns xAPI records and document resources; Psychometrics Commons and mathematical engines own assessment state and numerical measurement work.

## Current baseline

| Area | Evidence | Status | Commercialization gap | Next verification |
| --- | --- | --- | --- | --- |
| Repository authority | ADR 0001, README, ARCHITECTURE | Defined | Consumer dependency/versioning policy still needs executable release evidence | Merge bootstrap PR through protected `develop`, then publish an immutable versioned contract release |
| Learning event envelope | `schemas/v1/learning-event.schema.json` uses versioned path `v1`, `x-cwl-schema-version: 1.0.0`, and immutable logical `$id` `urn:contextualwisdomlab:learning-interoperability-contracts:learning-event:1.0.0` | Bootstrap candidate, not released/implemented evidence | The logical identifier is no longer mutable, but no protected release bundle currently binds version `1.0.0` to an immutable supported artifact | Establish the first protected immutable release and publish a machine-readable version-to-artifact/provenance mapping before consumers treat the URN as a supported release |
| JSON Schema validity | Quality workflow pins `jsonschema==4.26.0` and `rfc3339-validator==0.1.4`, runs `Draft202012Validator.check_schema`, and includes a negative metaschema regression | Candidate validation; live external merge gate | A passing predecessor head cannot establish current-head evidence; portable consumer behavior still depends on an explicit format-assertion policy | At merge time re-fetch the exact current head and require successful quality/security/SAST/review evidence; add consumer conformance fixtures before release |
| Timestamp contract | Range-constrained lexical pattern plus repository `Draft202012Validator(..., format_checker=FormatChecker())`, an activation check for impossible dates, parser-backed calendar checks, and positive/negative edge cases | **Blocked for portable consumer contract; repository gate implemented** | The committed lexical pattern intentionally does not encode month-specific/leap-year calendars, and JSON Schema 2020-12 `format` may be annotation-only for consumers that do not enable format assertion. The repository gate rejects impossible dates, but that alone does not prove equivalent cross-language consumer behavior | Keep the repository negative fixtures for invalid dates, leap-year boundaries, times and UTC offsets; define and execute a portable consumer format-assertion/conformance fixture contract before promoting this surface to released candidate |
| Standards portfolio | `docs/doctoring/STANDARD_TRACEABILITY.md`, AGENTS.md | Adoption decisions recorded; conformance not evidenced | Adoption and implementation evidence are separated; requirement-level executable evidence is still absent for unimplemented surfaces and QTI Metadata still needs a requirement-level source before implementation | Pin exact normative requirements/test paths as each surface becomes executable; never promote adoption to conformance without exact-head evidence |
| xAPI/cmi5 interoperability | Issue #3; cmi5 Quartz source pinned to release commit `984a9b8` in standards traceability | Planned | No executable xAPI 2.0/profile baseline on protected `develop` | Implement issue #3 after bootstrap lands; keep cmi5 Quartz/xAPI 1.0.3 compatibility distinct |
| CEFR assessment profile | PR #5 stacked on bootstrap; issue #4 | Candidate on stacked draft branch | Cannot be merge-ready until bootstrap lands and the stack is deliberately rebased/retargeted and reverified | Merge bootstrap first, restack PR #5 onto protected `develop`, rerun exact-head checks and independent review |
| Generated SDKs and cross-repository conformance | Issue #6 | Planned | No released Rust/TypeScript/Python generated contracts or consumer-driven interoperability proof | Implement after the core CEFR profile, preserving contract-only repository boundary |
| Release/package evidence | No protected released contract baseline yet | Missing | Consumers cannot pin an immutable supported contract release even though the schema now has an immutable logical URN | Establish first release, changelog/version policy, version-to-artifact mapping, provenance/SBOM where applicable, and immutable release receipts |
| Operability/security | Security/SAST workflows exist | Live external gate | No runtime service belongs here; committed CI status would become stale immediately | Keep repository read-only at runtime and require current-head supply-chain/security/generated-artifact evidence at merge/release time |

## DDD/context map

This repository is a generic interoperability subdomain. Its bounded context is **Learning Contract Authority**. Its ubiquitous language includes `contract_version`, `schema_version`, `profile_version`, `provenance_reference`, `compatibility_surface`, and `conformance_fixture`. Contract schemas and profile definitions are versioned value objects; released contract bundles are immutable release aggregates. Consumer repositories integrate through released artifacts only and must not acquire this repository's internal build tooling or cross-read another product database.

No shared-kernel database is permitted. Compatibility adapters belong in the consuming/owning runtime boundary unless the output is itself a reusable versioned interoperability mapping; such mappings may live here but remain non-authoritative for source application state.

## Release gates

A commercialization claim for a contract surface requires all of the following on the exact candidate head: schema/metaschema validation, positive and deliberately invalid fixtures, provenance/version invariants, applicable standards traceability, security/SAST checks, independent review, and an immutable release identifier bound to an immutable released artifact. A product adoption decision is not implementation conformance, and implementation conformance is not third-party certification.

## Active gap order

1. Land bootstrap PR #1 only after its live current-head checks and unresolved review gates are satisfied.
2. Establish the first immutable release bundle and version-to-artifact/provenance mapping for the already-versioned schema URN.
3. Add portable/cross-language timestamp conformance fixtures that make the required format-assertion behavior executable for consumers.
4. Deliver issue #3 executable xAPI 2.0/profile conformance while retaining the cmi5 Quartz/xAPI 1.0.3 compatibility boundary.
5. Restack and verify PR #5 for issue #4 after the bootstrap parent is protected-branch truth.
6. Implement issue #6 generated SDKs and cross-repository consumer conformance.
7. Continue replacing moving standards overview links with revision/requirement-level normative evidence as each surface becomes executable.
