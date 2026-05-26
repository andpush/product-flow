# General Rules
<!-- Seed for the `arch` skill. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent backend engineer. -->

## Coding rules

- Avoid duplications, use DRY principle
- Avoid artificial complexity, stick to KISS/YAGNI principles
- Prefer immutable data structures

**Surgical Changes:**

- Touch only what you must. Match existing style.
- Minimum code/complexity that solves the problem.
- Don't refactor unrelated code.
- Remove imports/functions/variables that YOUR changes made unused.
- Every changed line should trace directly to the request.

## Documentation rules

Consider updating the documentation after significant changes:

- `README.md` - project overview for a quick start for developers and must contain: purpose, components, commands and tools.
- `ADR.md` - keeps track of major architectural changes and decisions. Add a record in case of: significant change in design, tech stack, dependencies, integrations, DB schema, or testing approach.
