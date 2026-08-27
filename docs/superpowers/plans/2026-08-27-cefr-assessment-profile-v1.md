# CEFR Language Assessment Profile v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a versioned, executable CWL contract for CEFR-aligned and empirically CEFR-linked language assessment blueprints and result snapshots.

**Architecture:** The contracts repository owns JSON Schemas, conformance fixtures, deterministic cross-field validation, and standards traceability only. Psychometrics Commons remains the assessment authority, `fast-mlsirm` remains the numerical authority, and the LMS consumes an opaque immutable result reference rather than recalculating CEFR levels.

**Tech Stack:** JSON Schema Draft 2020-12, Python 3 standard library quality validation, GitHub Actions, Markdown doctoring.

**Spec:** `docs/superpowers/specs/2026-08-27-cefr-assessment-profile-design.md`

## Global Constraints

- Target branch stack: `agent/bootstrap-learning-contracts` → `feat/cefr-assessment-profile-v1`.
- Do not copy CEFR descriptor prose or language-specific RLD content into schemas or fixtures.
- Do not introduce a `cefr_certified` state or imply Council of Europe certification.
- CEFR level labels are ordinal labels and may not be averaged as integers.
- `cefr_linked` claims require familiarisation, specification, standardisation, standard-setting, empirical-validation, and cut-score evidence references.
- High-stakes use requires `cefr_linked`, human-review policy, and decision-use limitations.
- The repository owns no runtime database or product state.
- Every JSON Schema uses Draft 2020-12, `additionalProperties: false`, and an immutable schema-version marker.
- Validation is deterministic and fail-closed; it never repairs, renormalizes, or invents evidence.

---

### Task 1: Add CEFR assessment blueprint contract

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/README.md`
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/cefr-assessment-blueprint.schema.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/valid/diagnostic-blueprint.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/valid/linked-blueprint.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/high-stakes-aligned-blueprint.json`

**Interfaces:**
- Consumes: repository contract authority from `docs/adr/0001-contract-authority-boundary.md`.
- Produces: schema ID `cwl_cefr_assessment_blueprint/v1`, closed domain/level vocabularies, and linking-evidence references consumed by Task 2.

- [ ] **Step 1: Add a diagnostic blueprint fixture before the schema**

Create a valid English A1-B2 placement blueprint measuring reading, listening, written production, and spoken production. Set `claim_status` to `cefr_aligned`, keep overall reporting `profile_only`, and use descriptor/RLD references without descriptor text.

- [ ] **Step 2: Add a linked blueprint fixture**

Create a second fixture with `claim_status: cefr_linked` and exact familiarisation, specification, standardisation, standard-setting, empirical-validation, and cut-score-policy references.

- [ ] **Step 3: Add a failing high-stakes aligned-only fixture**

Create a fixture whose purpose is `high_stakes` but whose claim is only `cefr_aligned`; the conformance validator must reject it with `CEFR-BP-006`.

- [ ] **Step 4: Implement the blueprint JSON Schema**

Define exact identities, framework revision, BCP 47 language tag, purpose, level range, domain specifications, descriptor/RLD references, response/scoring modes, accessibility reference, overall-reporting policy, and linking evidence. Use `if`/`then` to require the linking evidence object for `cefr_linked` and to prohibit high-stakes aligned-only blueprints.

- [ ] **Step 5: Validate JSON syntax and schema metadata**

Run:

```bash
python -m json.tool profiles/cwl_cefr_language_assessment/v1/schemas/cefr-assessment-blueprint.schema.json >/dev/null
python -m json.tool profiles/cwl_cefr_language_assessment/v1/conformance/valid/diagnostic-blueprint.json >/dev/null
python -m json.tool profiles/cwl_cefr_language_assessment/v1/conformance/valid/linked-blueprint.json >/dev/null
```

Expected: all commands exit 0.

- [ ] **Step 6: Commit**

```bash
git add profiles/cwl_cefr_language_assessment/v1
git commit -m "feat: add CEFR assessment blueprint contract"
```

### Task 2: Add CEFR result snapshot contract

**Files:**
- Create: `profiles/cwl_cefr_language_assessment/v1/schemas/cefr-result-snapshot.schema.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/valid/diagnostic-result.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/valid/linked-result.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/probability-sum-result.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/duplicate-domain-result.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/missing-required-domain-overall-result.json`
- Create: `profiles/cwl_cefr_language_assessment/v1/conformance/invalid/certification-claim-result.json`

**Interfaces:**
- Consumes: blueprint IDs and claim/linking evidence from Task 1.
- Produces: schema ID `cwl_cefr_result_snapshot/v1`, domain-level uncertainty, overall-reporting policy reference, and immutable assessment-result handoff fields for Psychometrics Commons and LMS consumers.

- [ ] **Step 1: Add valid diagnostic and linked result fixtures**

The diagnostic result reports domain profiles only. The linked result carries standard-setting and cut-score revision references. Each measured domain includes a reported level, probability distribution summing to 1, uncertainty, and descriptor coverage references.

- [ ] **Step 2: Add invalid cross-field fixtures**

Create fixtures for a probability total unequal to 1, duplicate domain codes, an overall level despite a missing required domain, and an explicit certification claim.

- [ ] **Step 3: Implement the result JSON Schema**

Define immutable assessment/provenance references, closed level/domain vocabularies, non-reportable states, probability entries, uncertainty, credible level set, descriptor coverage, human review, limitations, and overall result. Exclude arithmetic-mean aggregation from the vocabulary.

- [ ] **Step 4: Validate JSON syntax**

Run `python -m json.tool` for the schema and every fixture. Expected: every file is syntactically valid JSON, including fixtures that are semantically invalid.

- [ ] **Step 5: Commit**

```bash
git add profiles/cwl_cefr_language_assessment/v1
git commit -m "feat: add CEFR result snapshot contract"
```

### Task 3: Add deterministic conformance validation

**Files:**
- Create: `scripts/validate_cefr_contracts.py`
- Create: `tests/test_cefr_contracts.py`
- Modify: `.github/workflows/quality.yml`

**Interfaces:**
- Consumes: Task 1 and Task 2 schemas and fixture directories.
- Produces: deterministic invariant codes `CEFR-BP-*` and `CEFR-RS-*`; exact-head workflow evidence.

- [ ] **Step 1: Write tests for valid fixture acceptance**

Tests import `scripts.validate_cefr_contracts`, load both valid blueprint/result fixtures, and assert an empty error list.

- [ ] **Step 2: Write tests for each invalid fixture**

Assert the expected invariant code:

```text
CEFR-BP-006 high-stakes aligned-only
CEFR-RS-003 probability sum
CEFR-RS-004 duplicate domain
CEFR-RS-007 overall with missing required domain
CEFR-RS-009 certification claim
```

- [ ] **Step 3: Run tests and confirm failure**

Run:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Expected: import or missing-validator failures before implementation.

- [ ] **Step 4: Implement the validator**

Implement pure functions for loading artifacts, validating blueprint invariants, validating result invariants, checking decimal probability totals, detecting forbidden certification claims recursively, and validating all repository fixtures by directory classification. Error messages include invariant code and file path. The command exits nonzero when a valid fixture fails or an invalid fixture is accepted.

- [ ] **Step 5: Run tests and the repository validator**

Run:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_cefr_contracts.py
```

Expected: all tests pass and the command prints the count of accepted valid fixtures and rejected invalid fixtures.

- [ ] **Step 6: Wire the exact-head GitHub workflow**

Replace the long inline bootstrap-only validation with a bootstrap metadata check plus:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_cefr_contracts.py
```

The workflow must still validate every JSON file and required documentation marker.

- [ ] **Step 7: Commit**

```bash
git add scripts tests .github/workflows/quality.yml
git commit -m "test: enforce CEFR contract conformance"
```

### Task 4: Add standards, architecture, and consumer traceability

**Files:**
- Create: `docs/adr/0002-cefr-assessment-profile-boundary.md`
- Create: `docs/doctoring/CEFR_TRACEABILITY.md`
- Modify: `README.md`
- Modify: `docs/ARCHITECTURE.md`
- Modify: `docs/doctoring/STANDARD_TRACEABILITY.md`
- Modify: `CHANGELOG.md`

**Interfaces:**
- Consumes: all implemented contracts and validator evidence.
- Produces: repository-level decision and the dependency contract for subsequent Psychometrics Commons and LMS stacked PRs.

- [ ] **Step 1: Record the ADR**

Accept the contract-authority boundary, licensing rule, aligned-vs-linked claim distinction, non-certification rule, and numerical ownership boundary.

- [ ] **Step 2: Add CEFR traceability**

Map the Companion Volume, relating-examinations manual, tests/examinations guidance, and language-specific RLD registry to product decisions, schemas, fixture evidence, known limitations, and consumer repositories. Use APA 7th references and official Council of Europe sources.

- [ ] **Step 3: Update repository navigation and architecture**

Document the CEFR profile location, explain that descriptor prose is not redistributed, and list Psychometrics Commons/fast-mlsirm/LMS/Studio ownership.

- [ ] **Step 4: Update the changelog**

Add the CEFR blueprint, result snapshot, deterministic conformance validator, and standards traceability under `Unreleased`.

- [ ] **Step 5: Run all validation**

Run:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_cefr_contracts.py
git diff --check
```

Expected: all commands pass.

- [ ] **Step 6: Commit**

```bash
git add README.md CHANGELOG.md docs
git commit -m "docs: trace CEFR assessment contract decisions"
```

### Task 5: Open the stacked pull request and hand off consumers

**Files:**
- No repository file changes after the exact-head verification commit unless review finds a defect.

**Interfaces:**
- Consumes: exact head from Tasks 1-4.
- Produces: a PR targeting `agent/bootstrap-learning-contracts` and explicit follow-up boundaries for Psychometrics Commons, `fast-mlsirm`, Learning Content Studio, and Learning Management Platform.

- [ ] **Step 1: Verify the exact head and changed-file set**

Run the repository validation commands against the exact branch head and inspect `git diff agent/bootstrap-learning-contracts...HEAD` for unrelated changes.

- [ ] **Step 2: Open a non-draft stacked PR**

The PR body states that it is stacked on bootstrap PR #1, contains contracts and conformance evidence only, makes no CEFR-linking or certification claim for a real test, and requires independent current-head review and all protected checks.

- [ ] **Step 3: Create consumer follow-up work only after the contract PR exists**

Subsequent PRs consume the exact schema version:

```text
Psychometrics Commons
→ published CEFR instrument/result snapshot lifecycle

fast-mlsirm
→ multidimensional and many-facet numerical calibration/recovery evidence

Learning Content Studio
→ immutable task/rubric/descriptor-reference release contract

Learning Management Platform
→ opaque CEFR result reference and placement policy consumption
```

No consumer may duplicate the schema or embed descriptor prose.
