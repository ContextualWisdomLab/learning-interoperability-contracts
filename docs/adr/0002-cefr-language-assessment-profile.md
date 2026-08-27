# ADR 0002: Rights-safe CEFR language-assessment profile

## Status

Accepted for the active stacked PR; not protected-`develop` truth until merged.

Approved by: ContextualWisdomLab repository owner  
Approval date: 2026-08-27

## Context

CWL can compose learning management, content authoring, assessment hosting, psychometric estimation, model orchestration and longitudinal analysis. It lacks a shared contract for reporting a domain-level language-proficiency profile in relation to the Common European Framework of Reference for Languages (CEFR).

A naive contract would create material risks:

- copying official descriptor prose or translations into a public repository;
- treating CEFR as a single equally spaced numerical score;
- averaging incomplete skill results into one overall label;
- confusing alignment with empirical linking or certification;
- moving scoring arithmetic or result authority into an interoperability repository;
- leaking raw responses, audio, task content, provider payloads or PII.

## Decision

Create `profiles/cwl_cefr_language_assessment/v1` as a metadata-only, versioned interoperability profile.

The profile:

1. references the CEFR Companion Volume, language-specific Reference Level Description, descriptors, task/rubric releases, scoring profile, cut-score revision, standard-setting study and validation evidence by immutable opaque identity;
2. supports Pre-A1, A1, A2, A2+, B1, B1+, B2, B2+, C1 and C2 while keeping domain results explicit;
3. models reception, production, interaction and mediation through typed activity-domain codes;
4. requires level probabilities, uncertainty, credible-level sets and descriptor-coverage references for every measured domain;
5. prohibits a reported overall level unless required domains are complete and a versioned overall-reporting policy is pinned;
6. requires standard-setting and linking-validation references before `cefr_linked` or certification-decision claims;
7. requires standard-setting evidence for high-stakes or certification blueprints;
8. rejects copied descriptor/task/response payload fields in fixtures and the quality gate;
9. leaves numerical scoring in fast-mlsirm, instrument/result authority in Psychometrics Commons, content authority in Learning Content Studio, and learner actions in Learning Management Platform.

## Consequences

### Positive

- Consumers can exchange an auditable proficiency profile without cross-service SQL or payload duplication.
- Domain-level uncertainty and incomplete evidence remain visible.
- Rights and certification claims fail closed.
- Future target languages can use different RLD authorities without changing the common contract.

### Negative

- The profile cannot prove that an assessment is linked to the CEFR.
- Consumers must resolve referenced artifacts through their authorized owning systems.
- Full JSON Schema conformance tooling and generated SDKs remain a later release slice.

## Reversal conditions

A new major profile version is required if the CEFR framework representation, level system, domain taxonomy, claim semantics or result envelope changes incompatibly. New optional evidence references may be added compatibly only with conformance fixtures and consumer contract tests.
