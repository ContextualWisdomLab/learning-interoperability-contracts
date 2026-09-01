# ADR 0002: Explicit xAPI protocol binding without historical translation

- Status: Candidate
- Date: 2026-09-02
- Decision owner: Learning Contract Authority
- Tracks: issue #3

## Context

ContextualWisdomLab consumers need one reusable way to distinguish the canonical xAPI 2.0 contract from the existing cmi5 Quartz compatibility path. Treating the two as interchangeable would allow a consumer to infer that a cmi5/xAPI 1.0.3 record is an xAPI 2.0 record, or to silently rewrite historical evidence while crossing product boundaries.

The current authoritative standards evidence also differs by surface. ISO/IEC/IEEE 39274-1-1:2025 is the published international xAPI standard. cmi5 Quartz remains the AICC Quartz 1st Edition compatibility specification based on xAPI 1.0.3, while IEEE P9274.3.1 is still an active project authorization rather than an approved cmi5 standard. Adoption therefore must not be represented as equivalent implementation or certification evidence.

## Decision

Define `cwl_xapi_protocol_binding/v1` as a provider-neutral immutable value object in the Learning Contract Authority bounded context.

The contract has exactly two compatibility surfaces:

1. `xapi_2_0` — requires `xapi_version = 2.0.0`, `xapi_profile_format_version = 1.0.0`, and the pinned authority `ISO/IEC/IEEE 39274-1-1:2025`.
2. `cmi5_quartz` — requires `xapi_version = 1.0.3`, `xapi_profile_format_version = 1.0.0`, `cmi5_release = quartz-1st-edition`, and pinned cmi5 revision `984a9b8`.

The schema is closed (`additionalProperties: false`). xAPI 2.0 bindings reject cmi5-only fields, cmi5 bindings reject xAPI 2.0 version claims, unknown compatibility surfaces fail closed, and statement payloads are outside this value object.

No consumer may treat this protocol-selection contract as xAPI statement conformance, cmi5 launch/package conformance, third-party certification, or proof that a historical record can be translated between versions. Statement truth remains with the Learning Record Store or another owning runtime.

## DDD and integration consequences

`ProtocolBinding` is a value object, not a runtime aggregate. It has no database, repository, transaction, domain event, or mutable identity. The consumer-facing anti-corruption layer selects a version-specific adapter based on a released binding and then validates the actual protocol payload under the appropriate owning contract.

This keeps the shared kernel minimal: consumers share an immutable versioned contract artifact, not runtime code or persistence. A future full xAPI 2.0 profile/conformance slice may add statement/profile schemas and fixtures here only when they are reusable provider-neutral contracts.

## Test-first evidence

- `05bbb0936c4ecfb87b7400d73545722ca1137ec7` introduced the failing/executable regression specification before the schema and fixtures existed.
- `2bbb549f5dda58794af4979f9f15ae3f514e4249` added the closed Draft 2020-12 protocol-binding schema and positive/negative fixtures.
- `6334e925050c562e27cee0857fb37c85ee36bea0` wired the regression suite into repository Quality.
- `b90103ecdc0f6e31edbb957d18b308d1f521d267` broadened repository Quality to stacked pull requests so this child slice cannot evade exact-head validation merely because its base is another feature branch.

Exact-head GitHub checks and independent review remain required. These commits are implementation history, not a conformance or release claim.

## Rejected alternatives

- **One permissive `xapi` surface:** rejected because it erases the protocol/profile revision boundary.
- **Automatic 1.0.3-to-2.0 rewriting:** rejected because historical evidence would acquire semantics it did not originally assert.
- **Copy protocol selection into each consumer:** rejected because divergent version rules would recreate the interoperability gap this repository exists to own.
- **Put statements into the binding object:** rejected because statement truth belongs to runtime/LRS boundaries and would turn a reusable value object into an application-state contract.

## References

AICC. (n.d.). *cmi5 specification—Quartz, 1st Edition* (revision 984a9b8). GitHub. https://github.com/AICC/CMI-5_Spec_Current/blob/984a9b8/cmi5_spec.md

IEEE Standards Association. (2025). *ISO/IEC/IEEE 39274-1-1-2025: Information technology—Learning, education and training—Experience API—Part 1-1: Data and data model*. https://standards.ieee.org/ieee/39274-1-1/12268/

IEEE Standards Association. (n.d.). *P9274.3.1: Standard for learning technology—JavaScript Object Notation (JSON) data model format and Representational State Transfer (RESTful) web service for learner experience data—Part 3-1: cmi5*. https://standards.ieee.org/ieee/9274.3.1/11183/
