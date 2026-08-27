# CEFR Language Assessment Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a rights-safe CEFR assessment blueprint, task, and immutable domain-result contract with executable positive and negative fixtures.

**Architecture:** The contract repository carries metadata references and conformance evidence only. Learning Content Studio owns authored content, Psychometrics Commons owns sessions/results, fast-mlsirm owns numerical psychometrics, LMS owns placement/completion actions, and TEPP owns longitudinal analysis.

**Tech Stack:** JSON Schema Draft 2020-12, JSON fixtures, Markdown ADR/doctoring, GitHub Actions with Python 3 standard library.

**Spec:** `docs/superpowers/specs/2026-08-27-cefr-language-assessment-profile-design.md`

## Global Constraints

- Target branch remains the bootstrap PR branch until PR #1 integrates.
- No runtime database or application state.
- No official CEFR descriptor prose, translations, task content, responses, audio, provider payloads or PII.
- No Python/Rust numerical arithmetic.
- Every claim and artifact is version-pinned.
- Exact-head review and required checks remain mandatory.

---

### Task 1: Common CEFR definitions

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/cefr-common.schema.json`

**Interfaces:**
- Produces: CEFR level, activity-domain, communication-mode, language-tag, exact-reference, digest and timestamp definitions.

- [x] Define Pre-A1, A1/A2/B1/B2/C1/C2 and A2+/B1+/B2+ codes.
- [x] Define reception, production, interaction and mediation.
- [x] Define activity domains without descriptor prose.
- [x] Pin Draft 2020-12, schema version and published `$id`.

### Task 2: Blueprint and task contracts

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/assessment-blueprint.schema.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/task-specification.schema.json`

**Interfaces:**
- Consumes: common definitions from Task 1.
- Produces: immutable assessment and task metadata boundaries.

- [x] Require target-language RLD, instrument, scoring, cut-score and validation references.
- [x] Require standard-setting evidence for high-stakes/certification blueprints.
- [x] Require mode-specific task evidence and rubric references for constructed responses.
- [x] Prohibit copied descriptor/task payload fields by closed schemas.

### Task 3: Immutable result contract

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/cefr-result-snapshot.schema.json`

**Interfaces:**
- Consumes: common definitions from Task 1.
- Produces: `cwl_cefr_language_assessment/result_snapshot/v1`.

- [x] Require domain probabilities, uncertainty and descriptor coverage for measured domains.
- [x] Require explicit non-measurement states instead of invented scores.
- [x] Gate overall reporting on complete required domains and a reporting policy.
- [x] Gate `cefr_linked` and certification claims on standard-setting and empirical validation references.

### Task 4: Positive and negative fixtures

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/valid/*.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/*.json`

**Interfaces:**
- Produces: executable examples for downstream contract tests.

- [x] Add an English A1–B2 placement blueprint.
- [x] Add a reference-only reading-task specification.
- [x] Add profile-only and linked-overall result examples.
- [x] Add failures for missing standard setting, copied descriptor text, incomplete overall reporting and non-unit probability mass.

### Task 5: Governance and traceability

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/README.md`
- Create: `docs/adr/0002-cefr-language-assessment-profile.md`
- Create: `docs/doctoring/CEFR_LANGUAGE_ASSESSMENT.md`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `docs/ARCHITECTURE.md`
- Modify: `docs/doctoring/STANDARD_TRACEABILITY.md`

**Interfaces:**
- Produces: reviewer-readable authority, rights, claim and research boundaries.

- [x] Record the 2020 Companion Volume and 2026 revised test-development manual.
- [x] State that the Council of Europe does not validate provider linking claims.
- [x] Separate CEFR alignment, linking and certification-decision status.
- [x] Record downstream repository ownership and next actions.

### Task 6: Executable fixture gate

**Files:**
- Modify: `.github/workflows/quality.yml`

**Interfaces:**
- Consumes: all Task 1–4 schemas and fixtures.
- Produces: `Learning Contracts Quality` exact-head evidence.

- [x] Parse every JSON file.
- [x] Verify schema metadata and published paths.
- [x] Accept all valid fixtures.
- [x] Reject each negative fixture for its intended reason.
- [x] Reject forbidden payload fields, duplicate domains and invalid probability mass.
- [ ] Obtain terminal hosted checks on the unchanged exact head.
- [ ] Obtain qualifying independent review after the parent branch is ready.
