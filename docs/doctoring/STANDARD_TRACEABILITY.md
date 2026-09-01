# Standards traceability

Adoption status and conformance evidence are intentionally separate. `Adopt` records a product decision; it does not imply implementation conformance or third-party certification.

| Standard or source | Revision | Normative or authoritative source | Scope | Adoption status | Evidence status |
|---|---|---|---|---|---|
| xAPI / ISO/IEC/IEEE 39274-1-1 | xAPI 2.0; ISO/IEC/IEEE 39274-1-1:2025 | https://www.iso.org/standard/91131.html | Canonical learning-experience record contract | Adopt | Not evidenced |
| cmi5 Quartz | Quartz, 1st Edition (2016), xAPI 1.0.3 compatibility | https://github.com/AICC/CMI-5_Spec_Current | Version-pinned LMS launch and package compatibility | Adopt as compatibility profile | Not evidenced |
| LTI Core | 1.3.0 Final | https://standards.1edtech.org/lti/specifications/core/lti-spec1p3p1 | External learning-tool launch and security contract | Adopt | Not evidenced |
| LTI Assignment and Grade Services | 2.0 Final | https://www.1edtech.org/standards/lti | Gradebook/result service interoperability | Adopt | Not evidenced |
| LTI Names and Role Provisioning Services | 2.0 Final | https://www.1edtech.org/standards/lti | Context-scoped membership and role provisioning | Adopt | Not evidenced |
| LTI Deep Linking | 2.0 Final | https://www.1edtech.org/standards/lti | Tool-mediated content selection and return | Adopt | Not evidenced |
| QTI Assessment, Section, and Item | 3.0.1 | https://www.1edtech.org/standards/qti/index | Assessment item/test interchange | Adopt | Not evidenced |
| QTI Metadata | 3.0 | https://www.1edtech.org/standards/qti/index | Assessment metadata interchange | Adopt | Not evidenced |
| CASE Service | 1.1 Final | https://standards.1edtech.org/case/ | Competency and learning-outcome interchange | Adopt | Not evidenced |
| Open Badges | 3.0 | https://www.1edtech.org/standards/open-badges | Portable achievement credential | Adopt | Not evidenced |
| Comprehensive Learner Record | 2.0 | https://www.1edtech.org/standards/clr | Portable learner achievement record | Adopt | Not evidenced |
| CEFR Companion Volume | 2020 | https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions | Framework, levels, communicative modes, descriptor-reference baseline | Adopt as reference-only profile | Contract fixtures on active PR; no assessment-linking claim |
| Manual for Language Test Development and Examining | Revised 2026 edition | https://www.coe.int/en/web/education/-/manual-for-language-test-development-and-examining-1 | CEFR-related language-test development baseline | Adopt for product/scientific traceability | Documentation only |
| Manual for Relating Examinations to the CEFR | 2009 edition | https://www.coe.int/en/web/common-european-framework-reference-languages/relating-examinations-to-the-cefr | Familiarisation, specification, standardisation, standard setting and empirical validation | Adopt for linking-claim gate | No linking study evidenced |
| Highlights from the Manual for Relating Examinations to the CEFR | 2012; ISBN 978-92-871-7169-6 | https://www.coe.int/en/web/common-european-framework-reference-languages/relating-examinations-to-the-cefr | Fixed summary reference for examination-linking practice | Adopt for reviewer orientation | Documentation only |
| CEFR Speaking Content Analysis Grid | February 2014 | https://www.coe.int/en/web/common-european-framework-reference-languages/relating-examinations-to-the-cefr | Exact speaking-content analysis support artifact | Adopt when speaking-validation evidence uses it | Not evidenced |
| CEFR Writing Content Analysis Grid | Version 3.1 | https://www.coe.int/en/web/common-european-framework-reference-languages/relating-examinations-to-the-cefr | Exact writing-content analysis support artifact | Adopt when writing-validation evidence uses it | Not evidenced |
| CEFR English RLD registry / English Profile | Registry snapshot dated 2026-08-27; source exposes no single immutable programme edition | https://www.coe.int/en/web/common-european-framework-reference-languages/english | Target-language authority/source discovery for English; blueprint pins `english_profile_registry_snapshot_2026_08_27` | Adopt as exact dated source snapshot, not as a final empirical validity artifact | No descriptor prose copied; downstream English profile evidence required |
| A Core Inventory for General English | 2010; ISBN 978-0-86355-653-1 | https://www.eaquals.org/resources/a-core-inventory-for-general-english/ | Exact English content-specification forerunner retained for research traceability | Reference only; not silently substituted for the English Profile registry | Downstream content-validation evidence required |
| Standards for Educational and Psychological Testing | 2014 | https://www.testingstandards.net/ | Intended interpretation/use, validity, reliability/precision, fairness and reporting | Adopt for assessment governance | Downstream product evidence required |
| WCAG | 2.2, W3C Recommendation 2024-12-12 | https://www.w3.org/TR/WCAG22/ | Accessible learning and contract-facing web content | Adopt | Not evidenced |
| ATAG | 2.0, W3C Recommendation 2015-09-24 | https://www.w3.org/TR/ATAG20/ | Accessible authoring-tool contract | Adopt | Not evidenced |

The Council of Europe does not verify or validate an examination provider's CEFR link. This repository must not use the Council of Europe logo or the European emblem to imply certification or endorsement.

A target-language blueprint must pin an exact publisher revision, edition, digest-bound snapshot, or dated registry snapshot. Mutable aliases such as `latest`, `current`, `head`, or `main` do not satisfy the contract. A dated registry snapshot is a reproducibility boundary, not a substitute for task, standard-setting, linking, DIF/invariance, or classification-validation evidence.

Every implementation PR that claims conformance must link the precise standard revision, normative requirement, implementation location, and executable evidence. Certification claims require the applicable certification process and may not be inferred from implementation alone.
