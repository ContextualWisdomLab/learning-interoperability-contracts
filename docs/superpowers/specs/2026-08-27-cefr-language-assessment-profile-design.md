# CEFR Language Assessment Profile Design

- Status: Approved design, implemented on an active stacked PR
- Date: 2026-08-27
- Parent: `agent/bootstrap-learning-contracts`
- Issue: `#4`

## Goal

Create the smallest shared contract that allows CWL products to exchange a rights-safe, domain-level CEFR language-assessment profile while keeping content, assessment execution, numerical scoring, learner management and longitudinal analysis in their owning repositories.

## Architecture

```text
Council of Europe / target-language profile authority
        │ immutable references + fixed revision/snapshot
        ▼
Learning Interoperability Contracts
        │ Draft 2020-12 schemas + semantic fixtures
        ├────────► Learning Content Studio task metadata
        ├────────► Psychometrics Commons blueprint/result snapshot
        ├────────► fast-mlsirm scoring-profile input/output contract
        ├────────► Learning Management Platform placement reference
        └────────► TEPP longitudinal result references
```

The contract repository owns no runtime state and performs no numerical calculation.

## Components

### Common definitions

Typed CEFR levels, communicative modes, activity domains, language tags, exact references, digests and timestamps.

### Assessment blueprint

Pins intended purpose, stakes, target language, exact target-language RLD/profile authority and immutable revision/snapshot, supported levels, required domains, instrument release, scoring profile, cut-score revision, overall-reporting authority, standard-setting evidence and validation evidence.

### Task specification

Pins descriptor identities, target levels, mode/domain, response mode, task release/digest, rubric, rights, accessibility, cognitive/linguistic demand and evidence model without copying task or descriptor text.

### Result snapshot

Carries immutable domain-level statuses, level probabilities, credible level sets, standard errors, descriptor coverage, overall-reporting status, claim status and evidence references. It does not carry raw responses, raw scores, item/person/rater parameter arrays, likelihood traces or other scoring-engine internals.

A result snapshot does not authorize its own overall result. The validator resolves `assessment_blueprint_reference`, verifies source-version equality for instrument/scoring/cut-score/language fields, requires every blueprint domain to be measured, and requires the exact blueprint `overall_reporting_policy_reference` before accepting an overall result.

## Error handling

Contracts fail closed when:

- Draft 2020-12 rejects a required field, type, enum, closed-property or conditional rule;
- descriptor/task/response payload fields appear;
- a target-language profile uses a mutable revision alias;
- high-stakes or certification blueprints omit standard-setting evidence;
- measured domains omit probability/uncertainty/coverage evidence;
- probability mass is not one;
- duplicate domain identities appear;
- a result references an unknown or incompatible blueprint;
- an overall result is reported without blueprint authorization, exact policy equality or complete required domains;
- `cefr_linked` claims omit standard-setting or empirical linking validation;
- certification decisions omit an exact certification authority or policy.

## Testing

The quality workflow installs a minimal hash-locked validator set, checks each committed schema against the Draft 2020-12 metaschema, validates every positive and negative fixture through the correct schema with offline `$ref` resolution, then applies semantic gates for probability mass, unique domains, immutable profile revisions and blueprint authority. Standard-library `unittest` regressions lock the structural-schema and cross-artifact authorization failures. Generated SDK tests remain a later release slice.

## Scope exclusions

- official descriptor text or translations;
- CEFR logo or endorsement claim;
- task, rubric, audio or response storage;
- scoring, linking, DIF or uncertainty arithmetic;
- instrument/session/result persistence;
- LMS placement policy;
- LLM provider calls;
- longitudinal growth estimation.
