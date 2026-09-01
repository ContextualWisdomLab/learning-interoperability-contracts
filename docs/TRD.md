# Technical requirements document

## System responsibility

`learning-interoperability-contracts` is an artifact-oriented **Learning Contract Authority** bounded context. It produces versioned, provider-neutral schemas/profiles/mappings, fixtures and generated-client contracts. It is not a network service, runtime database or owner of learning-domain transactional state.

## Architecture

```text
                 Learning Contract Authority
                  /        |          \
        schema/profile   fixtures   release artifacts
             |             |              |
             +-------------+--------------+
                           |
                    released version
                           |
           +---------------+----------------+
           |               |                |
      LMS/Platform     Content Studio      LRS/other
      ACL/adapter       ACL/adapter        ACL/adapter
           |               |                |
      owning state     owning state      owning state
```

Shared-kernel scope is deliberately minimal: immutable contract artifacts only. Each consumer owns its anti-corruption layer, transaction boundaries and persistence.

## Domain model

### Core value objects

- `contract_version`: semantic version of one contract surface;
- `schema_identity`: immutable logical identifier derived from contract name and semantic version;
- `profile_version`: explicit version of a reusable profile surface;
- `compatibility_surface`: named version-specific compatibility boundary;
- `conformance_fixture`: positive or negative executable evidence for an owned invariant;
- `provenance_reference`: immutable identity of the exact released artifact/build evidence.

### Aggregate boundary

A **Contract Release Bundle** is the artifact-level aggregate. Once released, its contract identities, manifest and bytes are immutable. Mutable authoring of contracts occurs in Git branches/PRs; there is no runtime relational aggregate or database repository.

### Domain invariants

- a released logical contract version maps to exactly one immutable artifact identity;
- a contract artifact never claims ownership of another bounded context's runtime state;
- incompatible protocol versions cannot be silently coerced into one surface;
- unsupported/unknown versions fail closed;
- release metadata cannot claim `Implemented`, `Conformant` or `Certified` without the required evidence class;
- fixtures contain no real person/institution identifiers and no impermissibly copied normative text.

## Repository layout

- `schemas/<major>/...` — versioned general contract schemas;
- `profiles/<contract>/<major>/...` — versioned profile/compatibility contracts;
- `fixtures/<surface>/{valid,invalid}/...` — public conformance/contract fixtures;
- `tests/` — executable repository/consumer contract tests;
- `docs/adr/` — architecture decisions;
- `docs/doctoring/` — standards/research traceability;
- future `release/` or equivalent — machine-readable bundle manifests/provenance only after release contract is specified;
- future generated SDK directories — generated from released contract authority, never hand-maintained as divergent truth.

## Versioning and compatibility

Semantic version is explicit for every reusable public contract. Major versions represent incompatible contract identity. Minor/patch compatibility policy must be encoded per surface before the first supported release.

Logical `$id`/contract identifiers are immutable names, not mutable branch URLs. Support requires a separate immutable release mapping from logical version to exact artifact bytes/provenance.

Compatibility adapters remain version-specific. The issue #3 xAPI protocol-binding candidate keeps canonical xAPI 2.0 distinct from cmi5 Quartz/xAPI 1.0.3 and carries no xAPI statement payload.

## Validation

Current repository Quality must:

1. check required product/technical/architecture/traceability documents;
2. validate JSON Schema Draft 2020-12 metaschema semantics rather than JSON syntax only;
3. execute date-time format assertion plus lexical/calendar edge cases for the learning-event envelope;
4. execute additional surface-specific valid/invalid fixtures as they are introduced;
5. run on stacked pull requests as well as protected-default-branch PRs;
6. check out the exact PR head with persisted credentials disabled.

Executable SDK/conformance code introduced later must reach 100% production statement/branch coverage for touched surfaces and public documentation coverage, with warnings treated as defects rather than suppressed.

## Standards evidence

`docs/doctoring/STANDARD_TRACEABILITY.md` is the current evidence ledger. A standard may be adopted without implementation. Before `Implemented`/`Conformant` language is allowed, traceability must bind:

- precise versioned normative requirement;
- implementation location;
- executable positive/negative fixture or test;
- terminal-success exact-head CI receipt.

External certification is a separate state and cannot be inferred from local validation.

## Security and supply chain

- GitHub Actions use least-privilege read permissions unless a write is materially required;
- external actions and executable tooling are version/checksum pinned where practical;
- protected integration requires current-head central security/SAST/review evidence;
- generated packages/releases require provenance and SBOM appropriate to their dependency surface;
- no secrets or PII belong in contract fixtures;
- there is no runtime service attack surface in the current product boundary.

## Persistence

No relational persistence belongs to this bounded context. If an operational release registry is ever required, the authoritative source remains immutable release artifacts; registry/cache storage must be a projection behind an ACL. Generic one-word persistence object names are disallowed if such storage is introduced, and any relational design must remain normalized rather than becoming a cross-product shared kernel.

## Delivery and operability

No web service, compose stack, k6 target, GPU/CPU math path or Kubernetes runtime is warranted by the current artifact-only architecture. Those requirements become applicable only if the product boundary intentionally adds an executable service; such a decision requires a new ADR rather than incidental infrastructure.

## Current technical gaps

- no protected immutable release bundle/provenance mapping yet;
- no complete xAPI 2.0 statement/profile conformance surface;
- no portable cross-language timestamp fixture runner across supported consumer languages;
- no generated Rust/TypeScript/Python SDK release artifacts;
- no OpenAPI/AsyncAPI surface where a concrete reusable protocol endpoint/event contract warrants one;
- no consumer-driven cross-repository compatibility matrix.
