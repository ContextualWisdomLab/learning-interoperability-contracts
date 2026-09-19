# ADR 0001: Contract authority boundary

## Status

Proposed. This bootstrap branch is review evidence only; the decision is not protected-`develop` truth and has no release authority.

## Decision

Propose this repository as the single CWL authority for shared learning interoperability schemas, profiles, generated clients, and conformance fixtures. It does not own runtime learner, content, assessment, or learning-record state.

## Consequences

Consumer repositories may depend on released contracts without acquiring this repository's implementation internals. A breaking semantic change requires an explicit contract version rather than an in-place reinterpretation.
