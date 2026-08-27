# CEFR Language Assessment Profile Design

- Status: Approved design, implemented on an active stacked PR
- Date: 2026-08-27
- Parent: `agent/bootstrap-learning-contracts`
- Issue: `#4`

## Goal

Create the smallest shared contract that allows CWL products to exchange a rights-safe, domain-level CEFR language-assessment profile while keeping content, assessment execution, numerical scoring, learner management and longitudinal analysis in their owning repositories.

## Architecture

```text
Council of Europe / RLD authority
        │ immutable references
        ▼
Learning Interoperability Contracts
        │ schemas + fixtures
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

Pins intended purpose, stakes, target language, RLD, supported levels, required domains, instrument release, scoring profile, cut-score revision, standard-setting evidence and validation evidence.

### Task specification

Pins descriptor identities, target levels, mode/domain, response mode, task release/digest, rubric, rights, accessibility, cognitive/linguistic demand and evidence model without copying task or descriptor text.

### Result snapshot

Carries immutable domain-level statuses, level probabilities, credible level sets, standard errors, descriptor coverage, overall-reporting status, claim status and evidence references. It does not carry raw responses or psychometric parameters.

## Error handling

Contracts fail closed when:

- descriptor/task/response payload fields appear;
- high-stakes or certification blueprints omit standard-setting evidence;
- measured domains omit probability/uncertainty/coverage evidence;
- probability mass is not one;
- duplicate domain identities appear;
- an overall result is reported with incomplete required domains;
- `cefr_linked` or certification claims omit standard-setting or empirical linking validation.

## Testing

The quality workflow parses all JSON, validates exact schema metadata, executes valid and negative fixtures, checks probability mass/domain uniqueness, and scans for forbidden payload fields using the Python standard library only. This is the executable first contract slice; full generic JSON Schema conformance and generated SDK tests are a later release slice.

## Scope exclusions

- official descriptor text or translations;
- CEFR logo or endorsement claim;
- task, rubric, audio or response storage;
- scoring, linking, DIF or uncertainty arithmetic;
- instrument/session/result persistence;
- LMS placement policy;
- LLM provider calls;
- longitudinal growth estimation.
