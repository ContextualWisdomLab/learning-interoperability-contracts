# CWL CEFR Language Assessment Profile v1

This profile defines transport contracts for CEFR-aligned and empirically
CEFR-linked language-assessment blueprints and immutable result snapshots.

## Contract files

- `schemas/cefr-assessment-blueprint.schema.json`
- `schemas/cefr-result-snapshot.schema.json`
- `conformance/valid/`
- `conformance/invalid/`

Run the exact repository conformance checks with:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_cefr_contracts.py
```

## Authority boundaries

- Psychometrics Commons owns assessment publication, sessions, responses,
  scoring dispatch, human review, and immutable result snapshots.
- `fast-mlsirm` owns psychometric estimation, uncertainty, linking, DIF,
  rater-facet, and true-parameter recovery calculations.
- Learning Content Studio owns immutable tasks, rubrics, accessibility variants,
  and descriptor/RLD references.
- Learning Management Platform consumes an opaque result reference and placement
  policy; it does not calculate CEFR levels.
- This repository owns only versioned contracts and conformance evidence.

## Claim vocabulary

`cefr_aligned` means that construct, blueprint, tasks, and reporting references
are designed in relation to the CEFR, without claiming empirical level linking.

`cefr_linked` means that the named blueprint/result is backed by exact
familiarisation, specification, standardisation, standard-setting, empirical
validation, and cut-score evidence references.

No `cefr_certified` state exists. The Council of Europe does not certify an
assessment provider's claimed relationship to CEFR levels.

## Licensing boundary

The profile does not reproduce CEFR descriptor prose or language-specific
Reference Level Description content. It stores stable identifiers, revision
metadata, and source references. Any licensed descriptor/RLD content belongs in
the consuming product's governed content store under the relevant publisher's
terms.

## Interpretation boundary

The level vocabulary is ordinal:

```text
pre_a1, a1, a2, a2_plus, b1, b1_plus, b2, b2_plus, c1, c2
```

Consumers must not convert the labels to equally spaced integers and average
them. An overall result requires a named model-based aggregation policy and
cannot conceal a required domain that was not measured or lacked sufficient
evidence.
