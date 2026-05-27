# Solution Design Spec

**Title:** <Title>
**Date:** YYYY-MM-DD
**Status:** Draft | Ready to build | Done (YYYY-MM-DD)
**Target:** <components / area this touches>

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

*Decisions flagged as significant architectural changes that should be added verbatim to `ADR.md` by the build.*

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

*Affected/new entities / schema changes (DDL or type shapes) / required migrations.*

### UI changes  *[as appropriate]*

*Screens, components, routing/state. Visual tokens defer to `DESIGN.md`.*

### Error handling  *[as appropriate]*

*Failure modes and how they're handled — validation, retries, fallbacks, user-facing messages.*

### Testing approach

*What to test and at which layer, and how (frameworks, fakes, fixtures). Follow testing pyramid: unit tests > integration tests > e2e tests.*

*For a refactor: define safety net that locks current behavior before any code moves, and the per-commit migration order that keeps the suite green.*

### Open questions that block implementation *[if any]*

*Anything that should be resolved before building.*

## Verification

### Acceptance criteria

*Verifiable conditions. For a behavior change, observable conditions; for a refactor - behavior unchanged, suite green.*

- [ ] <e.g. "POST /x with body Y returns 201 and persists Z">
- [ ] <e.g. "`./gradlew test` green; no public API change">

### Definition of Done

The build (`/goal` or any executing agent) is done only when **every** box below holds — stop-conditions alongside the acceptance criteria.

- [ ] Tests written for the new/changed behavior and passing — `<test command>` green. *(refactor: characterization safety net + existing suite green.)*
- [ ] All acceptance criteria above met.
- [ ] No duplication, no dead code, no obvious security issues; consistent with `ARCHITECTURE.md`.
- [ ] Memory updated: inlined *Architectural changes* transcribed to `ADR.md`; deferred ideas to `IDEAS.md`; `README.md` and `ARCHITECTURE.md` updated to stay in sync if required.
- [ ] Spec `Status` flipped to `Done (YYYY-MM-DD)` — the final act, only once every box above holds.
- [ ] Changes committed with proper message.
