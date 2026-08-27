# CEFR Language Assessment Profile v1 Design

- Status: Approved implementation baseline
- Date: 2026-08-27
- Owner: `ContextualWisdomLab/learning-interoperability-contracts`

## Goal

Define the first versioned CWL contract for reporting language-assessment evidence in relation to the Common European Framework of Reference for Languages (CEFR) without copying CEFR descriptor text, treating ordinal level labels as equal-interval scores, or allowing a contract document to imply Council of Europe certification.

## Product boundary

This repository owns only shared schemas, fixtures, and conformance rules.

- Psychometrics Commons owns instrument publication, assessment sessions, responses, scoring dispatch, immutable score snapshots, and scientific publication gates.
- `fast-mlsirm` owns psychometric numerical estimation, uncertainty, linking, DIF, rater-facet, and recovery calculations.
- Learning Management Platform consumes an opaque, versioned assessment-result reference and never recalculates CEFR levels.
- Learning Content Studio owns language tasks, prompts, rubrics, reference-level-description links, accessibility variants, and immutable releases.
- Semantic Data Portal may catalog framework, descriptor, language-specific RLD, and evidence metadata but does not own assessment results.

No service may directly read another service's database to implement this profile.

## Normative references and licensing boundary

The profile identifies the CEFR Companion Volume (2020), the Council of Europe manual for relating examinations to the CEFR, and language-specific Reference Level Descriptions by stable reference and revision metadata.

The schemas and fixtures do not reproduce CEFR descriptor prose. Descriptor text remains under the Council of Europe or relevant RLD publisher's copyright. A consuming product stores approved references and separately governed licensed content where permitted.

The Council of Europe does not certify a provider's claimed relationship between a test and CEFR levels. This profile therefore permits `cefr_aligned` and `cefr_linked` claim states but no `cefr_certified` state.

## Contract set

### Assessment blueprint

`cefr-assessment-blueprint.schema.json` records:

- immutable blueprint identity and schema version;
- CEFR framework revision;
- target language using an exact BCP 47 tag;
- assessment purpose and supported level range;
- measured communicative domains;
- descriptor and language-specific RLD references;
- response and scoring modes;
- accessibility-profile reference;
- overall-reporting policy;
- CEFR alignment or linking evidence state.

A `cefr_linked` blueprint must reference familiarisation, specification, standardisation, standard-setting, and empirical-validation evidence. A `cefr_aligned` blueprint may be used for diagnostic research or pilot use but must not claim empirically established level cut scores.

### Result snapshot

`cefr-result-snapshot.schema.json` records:

- immutable learner-result and assessment references;
- exact framework, blueprint, instrument, scoring, calibration, and result-schema versions;
- target language and assessment purpose;
- one result per measured domain;
- reported level or an explicit non-reportable status;
- level-probability distribution, standard error, and interval evidence where available;
- descriptor-coverage references;
- overall result only through a named, versioned aggregation policy;
- known limitations and human-review state.

Arithmetic averaging of ordinal CEFR labels is not a supported aggregation policy. `cefr_linked` results require standard-setting and cut-score revision references. High-stakes results require `cefr_linked`, a human-review policy, and explicit decision-use limitations.

## Level vocabulary

The transport vocabulary supports:

```text
pre_a1
a1
a2
a2_plus
b1
b1_plus
b2
b2_plus
c1
c2
```

These values are ordered labels, not equal-interval numbers. Consumers must not convert them to integers and average them.

## Domain vocabulary

The initial closed vocabulary is:

```text
reading
listening
written_production
spoken_production
written_interaction
spoken_interaction
online_interaction
mediation
phonological_control
```

A profile may omit unmeasured domains, but every omission required by the blueprint must be reported as `not_measured` or `insufficient_evidence`; it may not be silently treated as a low score.

## Conformance rules beyond JSON Schema

The quality gate performs deterministic checks that JSON Schema cannot express conveniently:

1. domain codes are unique;
2. required blueprint domains are present in a result;
3. level probabilities use the declared vocabulary and sum to 1 within decimal tolerance;
4. a reported level has positive probability and belongs to the credible level set when supplied;
5. `cefr_linked` claims carry all linking evidence references;
6. high-stakes results cannot use `cefr_aligned` claims;
7. an overall result cannot be reported when a required domain is non-reportable;
8. no field or value contains `cefr_certified` or an equivalent certification claim;
9. descriptor references contain identifiers and source references, not embedded descriptor prose.

## Error model

Conformance failures are fail-closed and identify the artifact path and invariant code. Validators do not repair malformed results, infer omitted levels, renormalize probabilities, or invent evidence references.

## Testing

The repository includes:

- valid diagnostic A1-B2 profile and result fixtures;
- valid linked profile fixture with standard-setting evidence;
- invalid high-stakes aligned-only fixture;
- invalid probability-sum fixture;
- invalid duplicate-domain fixture;
- invalid overall-result-with-missing-required-domain fixture;
- invalid certification-claim fixture.

The GitHub quality workflow validates JSON syntax, schema metadata, fixture classification, deterministic conformance rules, documentation links, and unresolved placeholder markers on the exact current head.

## Out of scope for v1

- CEFR descriptor text distribution;
- language-specific item banks;
- scoring or cut-score arithmetic;
- speech recognition or acoustic-feature contracts;
- QTI item serialization;
- xAPI learning-event profiles;
- Open Badges or CLR issuance;
- formal certification by the Council of Europe, ALTE, 1EdTech, or another body;
- a claim that a particular test is empirically CEFR-linked before its evidence is approved.
