# Learning Interoperability Contracts

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ContextualWisdomLab/learning-interoperability-contracts)

Shared, versioned interoperability contracts for the CWL Learning Platform.

## Scope

This repository contains schemas, profiles, generated-client contracts, and conformance fixtures shared by the Learning Management Platform, Learning Content Studio, Learning Record Store, Psychometrics Commons, and other CWL consumers.

Initial standards portfolio: xAPI 2.0, cmi5 Quartz compatibility, LTI 1.3, QTI 3, CASE 1.1, Open Badges 3.0, CLR 2.0, and accessibility-related contract metadata.

It contains no product runtime state and no application database.

## Branching

Product work targets `develop`; release promotion to `main` occurs only after exact-head review and required checks.

See `docs/ARCHITECTURE.md` and `docs/doctoring/STANDARD_TRACEABILITY.md` before adding a contract.
