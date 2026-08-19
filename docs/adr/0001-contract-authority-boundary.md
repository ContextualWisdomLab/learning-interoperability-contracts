# ADR 0001: Contract authority boundary

## Status

Accepted

Approved by: ContextualWisdomLab repository owner  
Approval date: 2026-08-19

## Decision

This repository is the single CWL authority for shared learning interoperability schemas, profiles, generated clients, and conformance fixtures. It does not own runtime learner, content, assessment, or learning-record state.

## Consequences

Consumer repositories may depend on released contracts without acquiring this repository's implementation internals. A breaking semantic change requires an explicit contract version rather than an in-place reinterpretation.
