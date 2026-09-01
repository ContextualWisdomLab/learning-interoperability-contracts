# Standards traceability

Adoption status and implementation/conformance evidence are intentionally separate. `Adopt` records a product decision pinned to an identified specification revision; it does not imply implementation conformance or third-party certification. The issue #3 protocol-binding slice is therefore recorded only as an internal ContextualWisdomLab contract candidate until a precise normative requirement, implementation surface, executable fixture and terminal-success exact-head CI receipt can be bound together.

| Standard | Revision | Normative source | Scope | Adoption status | Evidence status |
|---|---|---|---|---|---|
| xAPI / ISO/IEC/IEEE 39274-1-1 | xAPI 2.0; ISO/IEC/IEEE 39274-1-1:2025 | https://standards.ieee.org/ieee/39274-1-1/12268/ | Canonical learning-experience record contract | Adopt | **No xAPI implementation/conformance claim.** Issue #3 PR #7 adds only the internal `cwl_xapi_protocol_binding/v1` candidate that selects the xAPI `2.0.0` surface and keeps it distinct from cmi5. Candidate location: `profiles/cwl_xapi_protocol_binding/v1/protocol-binding.schema.json`; executable internal invariant fixture: `tests/test_xapi_protocol_binding.py`. Terminal-success exact-head CI and requirement-level xAPI statement/profile evidence are still absent. |
| cmi5 Quartz | Quartz, 1st Edition (2016), xAPI 1.0.3 compatibility | https://github.com/AICC/CMI-5_Spec_Current/blob/984a9b8/cmi5_spec.md | Version-pinned LMS launch and package compatibility | Adopt as compatibility profile | **No cmi5 implementation/conformance claim.** Issue #3 PR #7 adds only the internal compatibility-selection candidate pinned to Quartz revision `984a9b8` and xAPI `1.0.3`; its negative fixtures reject xAPI 2.0 crossover. Terminal-success exact-head CI plus requirement-level launch/package evidence are still absent. IEEE P9274.3.1 remains an active PAR and is not represented as an approved standard. |
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

An adoption row may remain `Not evidenced (adoption only)` indefinitely if no implementation surface is introduced. Before an implementation PR can claim `Implemented`, `Conformant`, or equivalent language, it must pin the precise normative requirement, implementation location, executable fixture/test path, and terminal-success exact-head CI receipt. A moving overview page is insufficient evidence for a requirement-level implementation claim and must be replaced by the applicable versioned specification section when that surface is implemented. Certification claims additionally require the applicable external certification process and may not be inferred from adoption, implementation, passing local tests, or documentation alone.

## Research references (APA 7th)

AICC. (n.d.). *cmi5 specification—Quartz, 1st Edition* (revision 984a9b8). GitHub. https://github.com/AICC/CMI-5_Spec_Current/blob/984a9b8/cmi5_spec.md

IEEE Standards Association. (2025). *ISO/IEC/IEEE 39274-1-1-2025: Information technology—Learning, education and training—Experience API—Part 1-1: Data and data model*. https://standards.ieee.org/ieee/39274-1-1/12268/

IEEE Standards Association. (n.d.). *P9274.3.1: Standard for learning technology—JavaScript Object Notation (JSON) data model format and Representational State Transfer (RESTful) web service for learner experience data—Part 3-1: cmi5*. https://standards.ieee.org/ieee/9274.3.1/11183/
