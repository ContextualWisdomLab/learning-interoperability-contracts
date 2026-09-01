# Product and technical gap baseline

Last reconciled: 2026-09-02

This ledger is derived from the current product boundary, PRD/TRD, ADRs, standards traceability, open issues, open pull requests, and exact-head GitHub evidence. It is a commercialization planning artifact, not a conformance or certification claim. Live GitHub Check state is intentionally not persisted as `queued`/`running`/`passed` because it changes outside the repository; merge decisions must re-fetch the exact PR head and live required Checks.

## Product responsibility

`learning-interoperability-contracts` is the ContextualWisdomLab authority for versioned, provider-neutral learning interoperability contracts, schemas, profiles, mappings, conformance fixtures, and reproducible generated-client contracts. It owns no learner/application runtime state and no product database. Learning Management Platform owns enrollment/progression/completion policy; Learning Content Studio owns authored content and releases; Learning Record Store owns xAPI records/document resources; Psychometrics Commons and mathematical engines own assessment state and numerical measurement work.

## Exact-head stack evidence

- bootstrap PR #1 is open/Ready and currently points to `18ae68203047c65cd787c9f6c378e26db26ffe0f` on `agent/bootstrap-learning-contracts`;
- protocol-binding PR #7 was still based on predecessor parent `65561221d9210884d234e52edc3e023e93d3278d`, so GitHub reported it not mechanically mergeable before this reconciliation;
- the parent delta is one commit adding PRD/TRD and documentation/index/quality-baseline requirements; protocol-binding implementation itself remains a distinct seven-commit child slice;
- this stack is being converged non-destructively by regular merge ancestry, preserving both the parent PRD/TRD gate and the child protocol-binding regression suite;
- predecessor Quality/review evidence is lineage only after any writer-branch head move; fresh exact-head repository Quality, security/SAST, and independent review remain required.

## Current baseline

| Area | Evidence | Status | Commercialization gap | Next verification |
| --- | --- | --- | --- | --- |
| Product/technical authority | `docs/PRD.md`, `docs/TRD.md`, ADR 0001, README, ARCHITECTURE | **Defined on bootstrap writer branch and required by repository Quality** | Product support claims remain candidates until protected integration/release evidence exists | Exact-head Quality must prove docs/implementation consistency; future scope changes update PRD/TRD/ADR in the same PR |
| Learning event envelope | `schemas/v1/learning-event.schema.json`, immutable logical `$id` | Bootstrap candidate, not a protected release | No protected immutable bundle binds logical version `1.0.0` to supported artifact bytes/provenance | Establish first protected immutable release and machine-readable version-to-artifact/provenance mapping |
| JSON Schema validity | Pinned `jsonschema==4.26.0`, `rfc3339-validator==0.1.4`, Draft 2020-12 metaschema check and negative regression | Candidate validation | Portable consumer behavior still needs explicit format-assertion conformance | Re-fetch exact-head quality/security/review and add consumer conformance fixtures before release |
| Quality runner admission | Earlier `ubuntu-latest` exact head queued with no steps; canonical bootstrap switched to explicit `ubuntu-24.04` | Causal selector repair committed | Selector repair is not terminal-success evidence | Fresh exact-head Quality must acquire runner and complete all gates |
| Stacked PR repository quality | bootstrap workflow uses `pull_request: {}`; child adds xAPI fixture test | **Reconciled in stack** | Scheduled repository Quality remains distinct from central protected security/review | Require fresh terminal-success child exact-head Quality and ordinary central gates |
| Timestamp contract | lexical pattern + active format checker + parser-backed calendar cases | Repository gate implemented; portable contract still blocked | JSON Schema consumers can treat `format` as annotation; equivalent cross-language behavior unproven | Add portable cross-language assertion/conformance fixtures |
| Standards portfolio | `docs/doctoring/STANDARD_TRACEABILITY.md`, AGENTS.md | Adoption and bounded implementation evidence separated from conformance | Requirement-level evidence remains absent for unimplemented surfaces | Pin exact normative requirements/tests as each surface becomes executable |
| xAPI/cmi5 interoperability | issue #3; PR #7; RED/spec `05bbb093...`; schema/fixtures `2bbb549f...`; Quality integration `6334e925...`; ADR 0002 | **Partially implemented:** closed `cwl_xapi_protocol_binding/v1` distinguishes canonical xAPI 2.0 from cmi5 Quartz/xAPI 1.0.3 and rejects cross-version/unknown/payload-leak fixtures | No protected released binding artifact; no complete xAPI 2.0 statement/profile conformance surface; no consumer conformance | Fresh exact-head checks/review, then a later provider-neutral statement/profile conformance slice without absorbing LRS runtime truth |
| CEFR assessment profile | PR #5 stacked on bootstrap; issue #4 | Candidate draft | Cannot become merge-ready before parent protected truth and deliberate restack/reverification | Integrate bootstrap first, restack PR #5, rerun exact-head checks/review |
| Generated SDKs/cross-repo conformance | issue #6 | Planned | No released Rust/TypeScript/Python generated contracts or consumer proof | Implement after core reusable contracts with reproducible generation |
| Release/package evidence | no protected released contract baseline | Missing | Consumers cannot pin supported immutable contract bundle | Establish changelog/version policy, bundle manifest, provenance/SBOM as applicable, immutable release receipt |
| Operability/security | artifact-only repo; central Security/SAST workflows; least-privilege local Quality | External merge gate | No runtime service is warranted; central security/review remain independent | Keep runtime read-only boundary and require current-head supply-chain evidence at merge/release |

## DDD/context map

This repository is a generic interoperability subdomain whose bounded context is **Learning Contract Authority**. Ubiquitous language includes `contract_version`, `schema_identity`, `profile_version`, `protocol_binding`, `compatibility_surface`, `conformance_fixture`, and `provenance_reference`. Contract schemas/profile definitions/protocol bindings are versioned value objects; a released **Contract Release Bundle** is the immutable artifact-level aggregate. Consumer repositories integrate through released artifacts and own their runtime ACLs, transactions, and persistence.

`cwl_xapi_protocol_binding/v1` is an anti-corruption value object, not a runtime aggregate. It selects an explicit protocol/profile family before a consumer-specific adapter runs. xAPI statements, cmi5 launch/session state, learner identities, and persistence remain with owning runtimes. No historical record is silently translated between protocol versions. No shared-kernel database is permitted.

## Release gates

A commercialization claim for a contract surface requires exact-candidate schema/metaschema validation, positive and deliberately invalid fixtures, provenance/version invariants, applicable requirement-level standards traceability, security/SAST checks, independent review, and an immutable release identifier bound to immutable released bytes. Adoption is not implementation conformance; bounded protocol selection is not xAPI statement/profile conformance or third-party certification.

## Active gap order

1. Land bootstrap PR #1 only after its live current-head checks and review gates are satisfied.
2. Establish the first immutable release bundle and version-to-artifact/provenance mapping.
3. Complete issue #3 beyond protocol selection with provider-neutral xAPI 2.0 statement/profile conformance fixtures while retaining cmi5 Quartz/xAPI 1.0.3 as a separate compatibility path.
4. Add portable/cross-language timestamp conformance fixtures.
5. Restack/verify PR #5 for issue #4 after bootstrap is protected truth.
6. Implement issue #6 generated SDKs and cross-repository consumer conformance.
7. Continue replacing moving standards overview references with revision/requirement-level normative evidence as executable surfaces appear.
