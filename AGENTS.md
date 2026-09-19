# Agent development rules

- Preserve repository responsibility: contracts only, no application state or product-specific database ownership.
- Pin every standards adoption decision to a precise revision and authoritative source. Adoption is a product decision, not conformance evidence.
- Pin every implementation/conformance claim to the precise normative requirement, implementation location, executable fixture/test path, and exact-head CI evidence. Record absent evidence explicitly rather than inferring conformance from adoption or documentation.
- Maintain backward-compatible contracts where declared; incompatible changes require a new version.
- Do not silently translate historical learning records between xAPI versions.
- Generated SDKs must be reproducible from committed schemas.
- Production code introduced here requires 100% statement and branch coverage plus complete public API documentation.
- Database object naming rules are not applicable because this repository must not own a runtime database.
