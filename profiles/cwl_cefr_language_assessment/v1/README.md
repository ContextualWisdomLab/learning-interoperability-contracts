# CWL CEFR Language Assessment Profile v1

This profile defines shared **references and result envelopes**, not a CEFR examination, a scoring engine, or a certification claim.

## Purpose

The contract lets Learning Content Studio, Psychometrics Commons, fast-mlsirm, Learning Management Platform, Semantic Data Portal, TEPP, and other CWL components exchange a language-assessment blueprint, task metadata, and an immutable domain-level result without sharing application databases or copying protected assessment and descriptor content.

## Authority boundaries

| Artifact | Authority |
|---|---|
| CEFR framework, descriptors, official translations | Council of Europe or licensed source |
| Language-specific Reference Level Description | Its published authority |
| Task, prompt, media, rubric, rights | Learning Content Studio or assessment-content owner |
| Instrument publication, session, response, result snapshot | Psychometrics Commons |
| Psychometric estimation, rater/task/facet calibration, DIF, linking and uncertainty | fast-mlsirm |
| Enrollment, placement action, completion and credential reference | Learning Management Platform |
| Longitudinal and multilevel language-development analysis | TEPP |

## Claims

- `experimental`: research-only evidence.
- `cefr_aligned`: the blueprint references CEFR constructs, but no empirical linking claim is made.
- `cefr_linked`: exact standard-setting and empirical linking-validation artifacts are pinned.
- `certification_decision`: a governed high-stakes decision; the shared contract does not itself establish certification authority.

The Council of Europe does not verify or certify an examination provider's CEFR link. The Council of Europe logo or European emblem must not be used to imply endorsement.

## Rights and data minimization

Official descriptor prose, translations, authored task content, raw responses, audio, model output and PII are prohibited in this shared profile. Contracts carry immutable opaque references, digests, status, uncertainty and evidence identities only.

## Files

- `schemas/cefr-common.schema.json`
- `schemas/assessment-blueprint.schema.json`
- `schemas/task-specification.schema.json`
- `schemas/cefr-result-snapshot.schema.json`
- `conformance/valid/`
- `conformance/invalid/`

The executable fixture gate lives in `.github/workflows/quality.yml` and is intentionally standard-library-only.
