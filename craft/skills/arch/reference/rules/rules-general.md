# General Rules
<!-- Seed for the `arch` skill. Adapt and fold into ARCHITECTURE.md's Conventions section. -->

## Coding rules

- Avoid duplications, use DRY principle.
- Avoid artificial complexity, stick to KISS/YAGNI principles.
- Prefer immutable data structures.
- Ground the implementation on requirements. Strictly adhere to the provided context. Do not invent or hallucinate features, technologies, or dependencies that aren't specified.

**Surgical Changes:**

- Touch only what you must. Match existing style.
- Minimum code/complexity that solves the problem.
- Don't refactor unrelated code.
- Remove imports/functions/variables that YOUR changes made unused.
- Every changed line should trace directly to the request.
