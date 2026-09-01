# Architecture

This repository owns versioned learning interoperability contracts and no application runtime state.

Primary families: xAPI 2.0, cmi5 Quartz compatibility, LTI 1.3, QTI 3, CASE 1.1, Open Badges 3.0, CLR 2.0, and rights-safe CEFR language-assessment metadata.

Authority boundaries:
- Learning Management Platform: offerings, enrollment, progression, placement/completion policy, and credential references.
- Learning Content Studio: authoring state, tasks, rubrics, media, rights, and immutable releases.
- Learning Record Store: xAPI statements and document resources.
- Psychometrics Commons: assessment blueprints/instrument publication, sessions, responses, and immutable result snapshots.
- fast-mlsirm: psychometric estimation, many-facet calibration, standard-setting/cut-score evidence, linking, DIF, uncertainty, and recovery.
- Semantic Data Portal: rights-aware descriptor/RLD/competency catalog references where adopted.
- TEPP: longitudinal, temporal, multilevel, and multiple-membership language-development analysis.
- contextual-orchestrator: bounded AI-rater orchestration; its observations are evidence, not score authority.

The CEFR profile stores immutable references and bounded result-envelope summaries only. Allowed summaries include domain `level_probabilities`, `credible_level_set`, `standard_error`, measurement status, descriptor-coverage references, claim status, limitations, and evidence identities. The profile never stores official descriptor prose, authored task content, raw responses, audio, provider payloads, PII, item/person/rater parameter arrays, likelihood traces, raw scores, response-level calculations, or other scoring-engine internals.

A reported overall result is not self-authorizing. The executable validator resolves the exact immutable assessment blueprint and accepts an overall result only when that blueprint permits overall reporting, every required domain is measured, and the result cites the blueprint's exact reporting policy.

Consumers integrate through versioned contracts; cross-repository database access is not part of the architecture.
