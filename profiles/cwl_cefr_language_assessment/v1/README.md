# CWL CEFR Language Assessment Profile v1

This profile defines shared **references and result envelopes**, not a CEFR examination, a scoring engine, or a certification claim.

## Purpose

The contract lets Learning Content Studio, Psychometrics Commons, fast-mlsirm, Learning Management Platform, Semantic Data Portal, TEPP, and other CWL components exchange a language-assessment blueprint, task metadata, and an immutable domain-level result without sharing application databases or copying protected assessment and descriptor content.

## Authority boundaries

| Artifact | Authority |
|---|---|
| CEFR framework, descriptors, official translations | Council of Europe or licensed source |
| Target-language Reference Level Description/profile source and revision | Its published authority; a dated registry snapshot is allowed only when no edition identifier exists |
| Task, prompt, media, rubric, rights | Learning Content Studio or assessment-content owner |
| Instrument publication, session, response, result snapshot | Psychometrics Commons |
| Psychometric estimation, rater/task/facet calibration, DIF, linking and uncertainty | fast-mlsirm |
| Enrollment, placement action, completion and credential reference | Learning Management Platform |
| Longitudinal and multilevel language-development analysis | TEPP |

## Claims

- `experimental`: research-only evidence; no operational CEFR interpretation claim.
- `cefr_aligned`: the blueprint references CEFR constructs and an exact target-language profile source/revision, but no empirical examination-linking claim is made.
- `cefr_linked`: exact standard-setting and empirical linking/classification-validation artifacts are pinned.
- `certification_decision`: the result is already linked and also pins the exact governed certification authority and certification policy. The shared contract does not create that authority.

The Council of Europe does not verify or certify an examination provider's CEFR link. The Council of Europe logo or European emblem must not be used to imply endorsement.

## Overall reporting

A result cannot authorize its own overall level. The executable validator resolves the immutable assessment blueprint and accepts a reported overall result only when:

- the blueprint declares `overall_and_profile`;
- every blueprint-required domain has status `measured`;
- the result's `reporting_policy_reference` exactly equals the blueprint policy;
- all structural and probability/credible-set checks pass.

## Rights and data minimization

Official descriptor prose, translations, authored task content, raw responses, audio, model output and PII are prohibited in this shared profile. Contracts carry immutable opaque references, bounded domain probability/uncertainty summaries, digests, status, limitations and evidence identities only. Item/person/rater parameter arrays, raw scores, likelihood traces and response-level calculations remain outside the contract.

## Files

- `schemas/cefr-common.schema.json`
- `schemas/assessment-blueprint.schema.json`
- `schemas/task-specification.schema.json`
- `schemas/cefr-result-snapshot.schema.json`
- `conformance/valid/`
- `conformance/invalid/`
- `scripts/validate_cefr_profile.py`
- `tests/test_validate_cefr_profile.py`
- `requirements-contracts-ci-hashes.txt`

The executable gate lives in `.github/workflows/quality.yml`. It installs a minimal hash-locked Draft 2020-12 validator set, resolves schema references offline, validates every fixture structurally, then applies semantic and cross-artifact authority checks.
