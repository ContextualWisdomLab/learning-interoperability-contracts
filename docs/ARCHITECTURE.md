# Architecture

This repository owns versioned learning interoperability contracts and no application runtime state.

Primary families: xAPI 2.0, cmi5 Quartz compatibility, LTI 1.3, QTI 3, CASE 1.1, Open Badges 3.0, and CLR 2.0.

Authority boundaries:
- Learning Management Platform: offerings, enrollment, progression, completion policy.
- Learning Content Studio: authoring state and immutable releases.
- Learning Record Store: xAPI statements and document resources.
- Psychometrics Commons: assessment sessions, responses, and score snapshots.

Consumers integrate through versioned contracts; cross-repository database access is not part of the architecture.
