# CEFR language-assessment research and standards basis

## Product interpretation

The CEFR is a non-prescriptive reference framework and common meta-language for curriculum, materials and assessment. It describes six common levels and three plus levels, and the Companion Volume adds Pre-A1 and expands descriptors for mediation, online interaction, plurilingual/pluricultural competence, phonology and signing.

This repository does not reproduce the descriptor corpus. A contract stores only an immutable `descriptor_reference`, exact framework authority, exact target-language profile/RLD source identity, and an immutable publisher revision or dated source snapshot.

## Assessment-development boundary

The 2026 revised *Manual for Language Test Development and Examining—For use with the CEFR* is the Council of Europe/ALTE test-development baseline adopted by this profile. The separate 2009 *Manual for Relating Language Examinations to the CEFR* and its explicitly identified supporting grids provide transparent, cumulative procedures for supporting a linking claim. The Council of Europe does not verify or validate an examination provider's claimed link.

The product claim states therefore have different evidence gates:

```text
experimental
- research-only contract evidence; no operational CEFR interpretation claim

cefr_aligned
- the blueprint references CEFR constructs, descriptors, and a target-language profile;
- no empirical examination-linking claim is made

cefr_linked
- exact standard-setting evidence and empirical linking/classification-validation
  evidence are pinned in addition to the aligned blueprint

certification_decision
- the result is already CEFR-linked;
- an exact certification authority and certification policy are pinned;
- the governed decision and publication requirements of that authority are met
```

A label cannot advance by editing narrative copy. A `cefr_aligned` result does not become `cefr_linked` without standard-setting and empirical validation, and a linked result does not become a certification decision without a governed decision authority and policy.

## Language-specific content

Reference Level Descriptions are language-specific inventories of linguistic forms and communicative content. CEFR profile v1 requires every target-language blueprint to pin both:

```text
language_reference_level_description_reference
language_reference_level_description_revision
```

The revision must be an immutable publisher revision, edition, digest-bound snapshot, or dated registry snapshot. Mutable aliases such as `latest` or `current` are rejected. Version 1 has no no-RLD exception; introducing one would require an explicit contract change, new claim semantics, and positive/negative conformance fixtures.

The public Council of Europe English RLD registry identifies the English Profile programme but exposes no single immutable edition identifier. The English fixtures therefore pin the authority as `coe_rld_registry_english_profile` and the dated registry snapshot `english_profile_registry_snapshot_2026_08_27`. That snapshot is a source-discovery identity, not a claim that all English Profile research has become one fixed operational RLD edition.

For content-specification research, the exact published forerunner retained in doctoring is North, Ortega, and Sheehan's *A Core Inventory for General English* (2010; ISBN 978-0-86355-653-1). It is not silently substituted for the English Profile registry identity in the contract.

## Measurement governance

The 2014 *Standards for Educational and Psychological Testing* governs intended interpretation and use, validity evidence, reliability/precision, fairness, administration, reporting and the rights of test takers. CEFR alignment alone does not establish these properties.

The downstream scientific owner must evaluate, as applicable:

- multidimensional structure and local dependence;
- rater, task, criterion, occasion and scoring-engine facets;
- standard-setting and cut-score uncertainty;
- classification consistency and decision error;
- form linking and anchor stability;
- language, population, mode and accommodation DIF/invariance;
- human/AI rater drift and adjudication;
- true-parameter and classification recovery;
- longitudinal comparability before change interpretation.

## Fixed examination-linking sources

This profile does not use mutable labels such as “current manual and supplements.” It pins these exact sources where applicable:

- Council of Europe (2009), *Relating Language Examinations to the CEFR: A Manual*;
- Council of Europe (2012), *Highlights from the Manual for Relating Language Examinations to the CEFR* (ISBN 978-92-871-7169-6);
- Council of Europe, *CEFR Speaking Content Analysis Grid*, February 2014;
- Council of Europe, *CEFR Writing Content Analysis Grid*, version 3.1.

Additional Council materials require their own exact title, version/date, source, digest or snapshot identity before they enter a blueprint or validation record.

## APA 7th references

American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for educational and psychological testing*. American Educational Research Association.

Association of Language Testers in Europe. (2026). *New revised manual for language test development and examining: For use with the CEFR*. Council of Europe.

Council of Europe. (2009). *Relating language examinations to the Common European Framework of Reference for Languages: Learning, teaching, assessment (CEFR): A manual*. Council of Europe.

Council of Europe. (2012). *Highlights from the manual for relating language examinations to the CEFR*. Council of Europe. ISBN 978-92-871-7169-6.

Council of Europe. (2020). *Common European Framework of Reference for Languages: Learning, teaching, assessment—Companion volume*. Council of Europe Publishing.

North, B., Ortega, A., & Sheehan, S. (2010). *A core inventory for general English*. British Council and EAQUALS. ISBN 978-0-86355-653-1.

## Official sources

- https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions
- https://www.coe.int/en/web/common-european-framework-reference-languages/introduction-and-context
- https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors
- https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-reference-level-descriptions-language-by-language-components-and-forerunners
- https://www.coe.int/en/web/common-european-framework-reference-languages/english
- https://www.coe.int/en/web/education/-/manual-for-language-test-development-and-examining-1
- https://www.coe.int/en/web/common-european-framework-reference-languages/relating-examinations-to-the-cefr
- https://www.eaquals.org/resources/a-core-inventory-for-general-english/
