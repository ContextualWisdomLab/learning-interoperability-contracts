# Standards traceability

Adoption status and implementation/conformance evidence are intentionally separate. `Adopt` records a product decision pinned to an identified specification revision; it does not imply implementation conformance or third-party certification. `Not evidenced (adoption only)` is therefore the expected bootstrap state until a consumer-facing contract surface has requirement-level executable evidence on an exact head.

| Standard | Revision | Normative source | Scope | Adoption status | Evidence status |
|---|---|---|---|---|---|
| xAPI / ISO/IEC/IEEE 39274-1-1 | xAPI 2.0; ISO/IEC/IEEE 39274-1-1:2025 | https://www.iso.org/standard/91131.html | Canonical learning-experience record contract | Adopt | Not evidenced (adoption only) |
| cmi5 Quartz | Quartz, 1st Edition (2016), xAPI 1.0.3 compatibility | https://github.com/AICC/CMI-5_Spec_Current/blob/quartz/cmi5_spec.md | Version-pinned LMS launch and package compatibility | Adopt as compatibility profile | Not evidenced (adoption only) |
| LTI Core | 1.3.0 Final | https://standards.1edtech.org/lti/specifications/core/lti-spec1p3p1 | External learning-tool launch and security contract | Adopt | Not evidenced (adoption only) |
| LTI Assignment and Grade Services | 2.0 Final | https://standards.1edtech.org/lti/specifications/services/assignments_grades/assignment-grade-services-spec | Gradebook/result service interoperability | Adopt | Not evidenced (adoption only) |
| LTI Names and Role Provisioning Services | 2.0 Final | https://standards.1edtech.org/lti/specifications/services/names_roles/names-role-provisioning-spec | Context-scoped membership and role provisioning | Adopt | Not evidenced (adoption only) |
| LTI Deep Linking | 2.0 Final | https://standards.1edtech.org/lti/specifications/launch_messages/deep_linking/lti-deep-linking-spec | Tool-mediated content selection and return | Adopt | Not evidenced (adoption only) |
| QTI Assessment, Section, and Item | 3.0.1 | https://www.imsglobal.org/sites/default/files/spec/qti/v3/info/imsqti_asi_v3p0p1_infomodel_v1p0.html | Assessment item/test interchange | Adopt | Not evidenced (adoption only) |
| QTI Metadata | 3.0 | https://www.1edtech.org/standards/qti/index | Assessment metadata interchange | Adopt | Not evidenced (adoption only; requirement-level source must be pinned before implementation) |
| CASE Service | 1.1 Final | https://standards.1edtech.org/case/ | Competency and learning-outcome interchange | Adopt | Not evidenced (adoption only) |
| Open Badges | 3.0 Final | https://standards.1edtech.org/open-badges/ | Portable achievement credential | Adopt | Not evidenced (adoption only) |
| Comprehensive Learner Record | 2.0 Final | https://standards.1edtech.org/clr/ | Portable learner achievement record | Adopt | Not evidenced (adoption only) |
| WCAG | 2.2, W3C Recommendation 2024-12-12 | https://www.w3.org/TR/WCAG22/ | Accessible learning and contract-facing web content | Adopt | Not evidenced (adoption only) |
| ATAG | 2.0, W3C Recommendation 2015-09-24 | https://www.w3.org/TR/ATAG20/ | Accessible authoring-tool contract | Adopt | Not evidenced (adoption only) |

An adoption row may remain `Not evidenced (adoption only)` indefinitely if no implementation surface is introduced. Before an implementation PR can claim `Implemented`, `Conformant`, or equivalent language, it must pin the precise normative requirement, implementation location, executable fixture/test path, and exact-head CI receipt. A moving overview page is insufficient evidence for a requirement-level implementation claim and must be replaced by the applicable versioned specification section when that surface is implemented. Certification claims additionally require the applicable external certification process and may not be inferred from adoption, implementation, passing local tests, or documentation alone.
