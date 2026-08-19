# Agent development rules

- Preserve repository responsibility: contracts only, no application state or product-specific database ownership.
- Pin every standard claim to a precise revision and executable conformance evidence.
- Maintain backward-compatible contracts where declared; incompatible changes require a new version.
- Do not silently translate historical learning records between xAPI versions.
- Generated SDKs must be reproducible from committed schemas.
- Production code introduced here requires 100% statement and branch coverage plus complete public API documentation.
- Database object naming rules are not applicable because this repository must not own a runtime database.
