# Architecture

This repository owns versioned learning interoperability contracts and no application runtime state.

Primary families: xAPI 2.0, cmi5 Quartz compatibility, LTI 1.3, QTI 3, CASE 1.1, Open Badges 3.0, and CLR 2.0.

## Domain-driven design

**Subdomain:** generic interoperability.  
**Bounded context:** Learning Contract Authority.

The bounded context owns provider-neutral contract identities, versioned schemas/profiles/mappings, conformance fixtures, and reproducible generated-client contracts. It does not own learner state, content state, xAPI statement truth, psychometric computation, or product databases.

Ubiquitous language includes:

- `contract_version`: immutable semantic version of a released contract surface;
- `protocol_binding`: an immutable value object selecting one explicitly versioned protocol/profile family without translating a record;
- `compatibility_surface`: an explicitly bounded compatibility path such as cmi5 Quartz/xAPI 1.0.3;
- `normative_authority`: the pinned external specification authority used to define a contract choice;
- `conformance_fixture`: executable positive or negative evidence for one contract invariant.

Current value objects:

- `learning-event` envelope schema — provider-neutral event transport envelope candidate;
- `cwl_xapi_protocol_binding/v1` — mutually exclusive protocol-selection value object for canonical xAPI 2.0 versus cmi5 Quartz/xAPI 1.0.3 compatibility.

The protocol-binding value object is intentionally not an aggregate or transaction boundary: it carries no xAPI statement, launch session, learner, registration, content, score, or runtime state. A consumer uses it as an anti-corruption boundary before invoking its own version-specific adapter. Historical records are never silently rewritten between xAPI versions.

## Authority boundaries

- Learning Management Platform: offerings, enrollment, progression, completion policy.
- Learning Content Studio: authoring state, immutable content releases, and target publication.
- Learning Record Store: authoritative xAPI statements and document resources.
- Psychometrics Commons: assessment sessions, responses, and score snapshots.
- `learning-interoperability-contracts`: reusable versioned contract authority only.

## Context map

```text
Learning Contract Authority
        |
        +--> released xAPI 2.0 protocol/profile contract --> consumer xAPI 2.0 adapter
        |
        +--> released cmi5 Quartz compatibility contract --> consumer cmi5/xAPI 1.0.3 adapter

Consumer adapters --> owning runtime aggregate / persistence
```

Consumers integrate through versioned released contracts. They do not copy contract logic into a shared database, cross-read another product database, or treat this repository as runtime truth. Compatibility adapters remain in their owning runtime unless the reusable mapping itself is the versioned interoperability product.

## Persistence and transaction boundaries

This repository owns no relational persistence, database schema, or runtime transaction. Released contract bundles are immutable release aggregates at the artifact/repository boundary. If generated SDK artifacts are introduced, reproducibility and provenance belong to the release pipeline rather than a product database.
