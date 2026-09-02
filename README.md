# Learning Interoperability Contracts

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ContextualWisdomLab/learning-interoperability-contracts)

**Versioned, provider-neutral contracts that let ContextualWisdomLab learning products exchange evidence without sharing implementation ownership.**

Learning Interoperability Contracts is the shared contract authority for schemas, profiles, mappings, conformance fixtures, and generated-client contracts across the CWL Learning Platform. It defines what crosses product boundaries; it does not become the source of truth for learner state, authored content, learning records, psychometric computation, billing, or product databases.

> **Status:** pre-release bootstrap. An open branch or schema path is not an immutable published contract release.

## What this repository is for

Use this repository when two learning products need a stable, reviewable interoperability boundary that must survive independent implementation and release cycles.

The current portfolio tracks:

- xAPI 2.0 as the canonical learning-record adoption target;
- cmi5 Quartz as an explicit xAPI 1.0.3 compatibility profile rather than a silent translation into xAPI 2.0;
- LTI 1.3;
- QTI 3;
- CASE 1.1;
- Open Badges 3.0;
- CLR 2.0; and
- accessibility-related contract metadata.

A standards name in this list records adoption intent or contract scope. It is **not** by itself implementation, conformance, certification, endorsement, or production evidence.

## Current bootstrap contract

The foundation includes a versioned learning-domain event envelope at:

`schemas/v1/learning-event.schema.json`

Its logical identity is version-derived rather than branch-derived, and repository quality checks validate JSON Schema Draft 2020-12 semantics plus an executable RFC 3339/date-time boundary. The contract and its maturity remain source evidence until protected integration and an immutable release establish a distributable consumer authority.

## How products should consume contracts

Production consumers should depend on an **immutable released contract artifact/revision with verifiable provenance**, not a mutable branch, open pull request, sibling checkout, or copied source fragment.

Consumer applications own their own Anti-Corruption Layer and runtime state. This repository owns the shared wire/profile contract only. In particular:

- Learning Management Platform owns learner/enrollment/completion application state;
- Learning Content Studio owns authored content and publication authority;
- Learning Record Store owns canonical learning-record evidence;
- Psychometrics Commons owns assessment-session/response/result evidence;
- numerical psychometric estimation remains outside this contract repository; and
- no consumer may treat this repository as a shared application database.

Until the first protected immutable release exists, current branch files are suitable for review and development only, not as a claim of released ecosystem compatibility.

## Contributor quick start

Repository quality is intentionally lightweight and contract-focused. The canonical validation workflow is [`.github/workflows/quality.yml`](.github/workflows/quality.yml); it uses Python 3 with pinned `jsonschema==4.26.0` and `rfc3339-validator==0.1.4` to validate required documentation, every committed schema, immutable schema identity, semantic-version/path alignment, and timestamp behavior.

Before changing or adding a contract:

1. read the [architecture boundary](docs/ARCHITECTURE.md);
2. check [standards traceability](docs/doctoring/STANDARD_TRACEABILITY.md) for the normative source and current adoption status;
3. preserve versioned schema/profile identity and backward-compatibility rules;
4. add or update executable fixtures/conformance evidence with the contract; and
5. run the repository quality contract and require fresh exact-head CI before integration.

Do not copy official standards text, assessment content, descriptors, logos, or other rights-controlled material into a contract merely because the repository references that standard.

## Architecture and evidence boundary

This repository is a Shared Kernel for **interoperability contracts**, not for foreign product implementation. Contracts must be provider-neutral, versioned, provenance-aware, and narrow enough that consumers can validate them without importing another product's private runtime model.

Key evidence rules:

- `Adopted` does not mean `Implemented`.
- `Implemented` does not mean `Conformant`.
- local or repository conformance evidence does not mean third-party `Certified`.
- an open PR is not an immutable release.
- mutable branch URLs and sibling source trees are not production dependency authority.
- a future `Implemented` or `Conformant` claim must identify the normative requirement, implementation location, executable fixture/test, and exact-head evidence that supports it.

## Documentation

- [Architecture](docs/ARCHITECTURE.md) — contract ownership and integration boundaries.
- [Standards traceability](docs/doctoring/STANDARD_TRACEABILITY.md) — normative-source and adoption evidence.
- [Product and technical gap baseline](docs/product-technical-gap-baseline.md) — current maturity and commercialization gaps.
- [Public documentation landing](docs/index.md) — concise repository navigation and publication boundary.
- [CHANGELOG](CHANGELOG.md) — integrated source-history notes, not release evidence by itself.
- [GitHub Releases](https://github.com/ContextualWisdomLab/learning-interoperability-contracts/releases) — immutable published releases when available.

## Branch and release authority

Product work targets `develop`. Promotion to `main` occurs only through the repository's protected process after exact-head validation and applicable review/security gates. A source commit on either branch is not automatically a published consumer release; release/version/artifact provenance must agree on the exact protected source.

## License

ContextualWisdomLab-authored source and documentation in this repository are licensed under the [Apache License 2.0](LICENSE).

That repository grant does not relicense standards, schemas or assets copied from external authorities, generated material with separate terms, future package dependencies, certification marks, or external services. Every imported or derived component remains subject to independent provenance and commercial-license review.
