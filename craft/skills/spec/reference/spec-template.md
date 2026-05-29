# Solution Design Spec

**Title:** <Title>
**Date:** YYYY-MM-DD
**Status:** Draft | Ready to build | Done (YYYY-MM-DD)
**Target:** <components / area this touches>

## Review Brief

*The fast human-review surface — enough to approve the approach without reading the execution detail below. Keep it compressed; link down, don't restate.*

- **Building:** what changes and the value, in a line.
- **Approach:** the chosen solution in a sentence.
- **Key tradeoffs:** the decisions that were live and what was chosen, one line each → `### Key decisions & rejected approaches`.
- **Impact:** components / data / API touched; architectural change? yes/no + one line.
- **Out / risk:** main risk and what's explicitly not done → `### Non-goals`.

## Goal

*What this delivers, the expected behavior, the motivation and value.*

### Constraints & assumptions  *[as appropriate]*

*Hard constraints (tech, performance, compliance) and the assumptions the solution rests on.*

### Non-goals  *[as appropriate]*

*What this explicitly does not do, and briefly why. Deferred ideas go to `IDEAS.md` on build.*

## Solution

### Description

*Describe the solution approach.*

### Architecture  *[if any structural change]*

*ASCII diagram of components, boundaries, interactions, data flow - what applicable to depict the change.*

```text
<ascii>
```

### Key decisions & rejected approaches *[if any]*

*Brief summary ~ one line per decision. Rejected approaches should answer WHY?*

### Architectural changes *[if any]*

*Significant architecural changes in terse form.*

Add verbatim to `ADR.md` at implementation.

```markdown
## YYYY-MM-DD · [component] · Short title
**Decision:** one sentence — what we chose.
**Why:** one or two sentences — why it beat the alternative (and what was rejected).
```

### Affected components & files

*Not an exhaustive set: the build may discover more. Group by component; tree layout.*

- **<component>**
  - `<path>` — <briefly: changes>

### API contracts *[as appropriate]*

*Affected/new endpoints.*

### Data model & migrations *[as appropriate]*

*Affected/new entities / schema changes (DDL or type shapes) / required migrations. Note the source of truth / owner when an entity is new or its ownership shifts.*

### State & lifecycle  *[as appropriate]*

*State sets and transitions, who owns each transition, and lifecycle rules (creation, validity, expiry, deletion) — when the change introduces or alters them.*

### UI changes  *[as appropriate]*

*Screens, components, routing/state. Visual tokens defer to `DESIGN.md`.*

### Error handling  *[as appropriate]*

*Failure modes and how they're handled — validation, retries, fallbacks, user-facing messages.*

### Testing approach

*What to test and at which layer, and how (tools, mocks, fixtures).*

*For a refactor: define green safety net that locks current behavior before any code moves.*

### Open questions that block implementation *[if any]*

*Anything that should be resolved before building.*

## Verification

### Acceptance criteria

*Verifiable conditions. For a behavior change, observable conditions; for a refactor - behavior unchanged, suite green.*

- [ ] <e.g. "POST /x with body Y returns 201 and persists Z">
- [ ] <e.g. "`./gradlew test` green; no public API change">

### Definition of Done

*This section should be included unchanged for the build agent.*

The implementation is done only when **every** box below holds:

- [ ] Tests written for the new/changed behavior and passing green. *(refactor: characterization safety net + existing suite green.)*
- [ ] All acceptance criteria above met
- [ ] Code is buildable and runnable without errors
- [ ] `simplify` or similar skill invoked: no duplications, no dead code, no unjustified complexity
- [ ] `code-review` and `security-review` (or similar skill) agents spawed and finished, without pointing to any major issues
- [ ] Code is consistent with `ARCHITECTURE.md`
- [ ] Memory updated: inlined *Architectural changes* transcribed to `ADR.md`; deferred ideas to `IDEAS.md`; `README.md` and `ARCHITECTURE.md` updated to stay in sync if required
- [ ] Spec `Status` flipped to `Done (YYYY-MM-DD)` — the final act, only once every box above holds
- [ ] Changes committed with proper message
