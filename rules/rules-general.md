# General Rules

## Business Analysis Rules

- Focus on description from business stakholders perspective, avoid specifying implementation detailes unless they are constraints.
- Think about right-size decomposition of required features

## Coding Rules

- Act as an expert software developer and generate clean, idiomatic, and robust code following KISS, DRY, SOLID principles.
- Ground the implementation on requirements. Strictly adhere to the provided context. Do not invent or hallucinate features, technologies, or dependencies that aren't specified.
- Avoid artificial complexity: YAGNI principle - You Aren't Gonna Need It.
- Prefer immutable data structures.
- Use latest stable versions of all dependencies.
- Use monorepo with component folders (e.g. backend/, mobile/, web/) in the root.

## Documentation

- Consider updating the documentation after each significant change:
- `README.md` - project overview for a quick start for developers and must contain: purpose, components, commands and tools;
- `CHANGELOG.md` - log of significant for end-user changes, e.g. new feature added or critical bug fixed;
- `ADR.md` - keeps track of major architectural changes and decisions. Add a record in case of: pattern applied; changes in design, tech stack, dependencies, integrations, DB schema, or testing approach. Each entry concisely denotes: Date, Decision and Motivation.
- Every feature specification should indicate what components it affects
