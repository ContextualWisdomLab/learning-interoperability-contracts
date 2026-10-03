# Architecture

This repository proposes to own versioned learning interoperability contracts and no application runtime state. The authority boundary remains Proposed until protected integration.

Primary families: xAPI 2.0, cmi5 Quartz compatibility, LTI 1.3, QTI 3, CASE 1.1, Open Badges 3.0, and CLR 2.0.

Authority boundaries:
- Learning Management Platform: offerings, enrollment, progression, completion policy.
- Learning Content Studio: authoring state and immutable releases.
- Learning Record Store: xAPI statements and document resources.
- Psychometrics Commons: assessment sessions, responses, and score snapshots.

Consumers integrate through versioned contracts; cross-repository database access is not part of the architecture.

Repository conformance consumers are test-only evidence, not SDKs or runtime services. The Rust and TypeScript timestamp consumers read the same committed language-neutral fixture and own no product state, network boundary, generated contract or release authority.
