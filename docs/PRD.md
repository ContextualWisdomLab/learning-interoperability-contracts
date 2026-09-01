# Product requirements document

## Product

**Learning Interoperability Contracts** is the provider-neutral contract authority for the ContextualWisdomLab learning ecosystem. It gives product teams and external integrators immutable, versioned definitions for exchanging learning-domain data without sharing product databases or leaking one runtime's internal model into another.

## Customer problem

Learning products fail to compose commercially when every service independently interprets xAPI, cmi5, assessment, credential, content and learning-platform payloads. The resulting schema drift produces silent semantic loss, brittle point-to-point adapters, version ambiguity and buyer-visible integration failures.

The product must make the safe integration path easier than copying a schema or inferring another product's database model.

## Primary customers and jobs to be done

### ContextualWisdomLab product teams

- select a released contract and know exactly which semantic/version boundary it represents;
- validate produced and consumed payloads against executable positive and negative evidence;
- distinguish canonical contracts from explicitly supported compatibility surfaces;
- upgrade contracts without silently changing historical meaning;
- generate or consume typed SDK surfaces without importing another product's runtime state.

### External integrators and platform operators

- pin an immutable supported contract release;
- identify breaking versus compatible changes before deployment;
- reproduce validation results from public fixtures and release provenance;
- understand which standards are adopted, implemented, conformant, certified or intentionally unsupported without marketing ambiguity.

## Product principles

1. **Contracts, not runtime truth.** Learner, enrollment, content-authoring, xAPI statement-store, assessment and payment truth remain in owning bounded contexts.
2. **Immutable release identity.** A logical schema/profile identity is not a supported release until an immutable artifact and provenance receipt bind that identity to exact bytes.
3. **No silent translation.** Compatibility mappings must preserve the source protocol/version boundary; cmi5 Quartz/xAPI 1.0.3 may not be relabelled as xAPI 2.0 history.
4. **Fail closed.** Unknown versions, unsupported fields, semantic loss and missing evidence reject rather than degrade silently.
5. **Evidence-qualified claims.** Adoption, implementation, conformance and certification are distinct states.
6. **Provider neutrality.** Shared contracts must not encode a specific service's storage layout, internal class hierarchy or deployment topology.
7. **Public-safe fixtures.** Tests and documentation use synthetic/non-identifying examples and do not redistribute licensed specification text beyond permitted use.

## Core product capabilities

### Versioned contract authority

- semantic-versioned JSON Schema/OpenAPI/AsyncAPI/profile artifacts where appropriate;
- immutable logical identifiers derived from contract identity and semantic version;
- explicit compatibility and deprecation policy;
- deterministic release bundle/provenance mapping.

### Conformance evidence

- machine-valid schemas;
- positive and deliberately invalid fixtures for every owned invariant;
- consumer-driven cross-language fixtures where format behavior can differ by validator/runtime;
- requirement-level traceability before an `Implemented` or `Conformant` standards claim.

### Compatibility boundaries

- canonical xAPI 2.0 contract family;
- explicit cmi5 Quartz/xAPI 1.0.3 compatibility family;
- future LTI, QTI, CASE, credentials and accessibility-related mappings kept version-specific;
- anti-corruption boundaries in consumers rather than a shared runtime/database kernel.

### Generated client contracts

Rust, TypeScript and Python package boundaries may be generated only from released reusable contract authority. Generated output must be reproducible, version-bound and covered by consumer conformance evidence before it is advertised as supported.

## Current commercialization slice

The bootstrap parent establishes repository authority, a versioned learning-event envelope candidate, Draft 2020-12 validation, timestamp edge cases, architecture/ADR/standards evidence, explicit PRD/TRD and exact-head quality gates. Issue #3 / PR #7 adds a separate internal protocol-selection candidate for xAPI 2.0 versus cmi5 Quartz without claiming statement/profile conformance.

Neither surface is a released supported contract until the protected integration/release gates below complete.

## Release gates

A contract surface is commercially supportable only when the exact release candidate has:

- machine-valid schemas and required positive/negative fixtures;
- immutable logical version identity plus immutable release artifact mapping;
- applicable requirement-level standards traceability;
- successful exact-head repository quality, security/SAST and independent review evidence;
- reproducible package/bundle output and provenance/SBOM when executable/generated dependencies exist;
- compatibility/deprecation notes and a CHANGELOG entry;
- no unresolved substantive review thread.

## Success measures

- zero production integrations depend on cross-repository database reads;
- every supported contract is pinned by immutable version/artifact identity;
- every breaking contract change is mechanically detectable or deliberately versioned;
- every standards implementation claim has executable requirement-level evidence;
- consumer teams can reproduce contract validation without private infrastructure;
- no buyer-facing documentation represents an unreleased candidate as a supported release.

## Non-goals

- operating an LMS, LCMS, LRS or assessment service;
- storing authoritative learner/content/statement/score state;
- psychometric or mathematical computation;
- silently upgrading historical protocol records;
- copying proprietary or licensed normative text into fixtures;
- providing a generic integration database or enterprise service bus.

## Roadmap and issue linkage

1. **Issue #2 / PR #1:** protected bootstrap authority, PRD/TRD, release/provenance baseline.
2. **Issue #3 / PR #7:** explicit protocol selection, then provider-neutral xAPI 2.0 statement/profile conformance evidence.
3. **Issue #4 / PR #5:** CEFR assessment profile after parent authority is protected truth.
4. **Issue #6:** generated SDKs and cross-repository consumer conformance.
5. First immutable public contract release only after the complete release gates are evidenced on the protected candidate.
