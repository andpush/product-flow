---
name: arch
description: Use to define or derive project architecture, stack, and conventions in a durable way that the `spec` skill can rely on. (Triggers: "define the architecture", "choose the stack", "write ARCHITECTURE.md".)
---

Establish the durable engineering context a software project needs — architecture, component/module map, tech stack, and coding conventions — either by defining them with the user (greenfield) or deriving them from existing code (brownfield), and wiring CLAUDE.md/AGENTS.md as thin pointers.

Run once; again only when foundations change.

Consumes `PRODUCT.md` (from `forge prod`); produces `ARCHITECTURE.md`, which `spec` consumes. The design counterpart is the impeccable plugin (https://impeccable.style) — it owns the product's visual/UX design (DESIGN.md); `arch` owns the engineering architecture. Both apply to a project that has a UI.

## Well known files

| File | Holds | Created by |
|---|---|---|
| `PRODUCT.md` | purpose, users, constraints | `forge prod` (or `/impeccable teach`) |
| `ARCHITECTURE.md` | components, stacks, boundaries, layout, entrypoints, **conventions** |  this `arch` skill or manually |
| `ADR.md` \| `DECISIONS.md` | why choices were made | appended over time |
| `README.md` | human onboarding | human; read as a source |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | this `arch` skill or manually |

## Detect first

Map existing files before creating any: check casing/variants — `ARCHITECTURE.md` / `docs/architecture.md`, `ADR.md` / `DECISIONS.md` / `docs/adr/*`, plus `README.md`, `PRODUCT.md`, `CLAUDE.md`, `AGENTS.md`. Adopt the repo's names; if the repo already keeps conventions in their own file (`rules*.md`, `CONVENTIONS.md`), reference them from ARCHITECTURE.md instead of restating.

## Greenfield: define with the user

1. Read `PRODUCT.md` for purpose, users, constraints.
2. Propose architecture and stack — proven over trendy, complexity matched to the problem. Present real forks (monolith vs. services, pre-built vs. created, paid vs. open-source, datastore options, etc.) as pro/contra via `AskUserQuestion`; don't bikeshed settled defaults. Architecture and stack shape each other, so iterate to coherence: propose components with preliminary tech, validate the tech against the components, refine both. When drawing boundaries, keep the component dependency graph acyclic — if two components depend on each other, resolve it (merge, extract a shared piece, or invert a dependency).
3. Write `ARCHITECTURE.md` using [reference/architecture-template.md](reference/architecture-template.md).
4. Write the `Rules and Conventions` section of `ARCHITECTURE.md`, seeding from [reference/rules/](reference/rules/): always fold `rules-general.md`; others -- by applicability. Read each, adapt with the user via `AskUserQuestion`, keep only the non-obvious or project-specific.

## Brownfield: derive from the code, then confirm

1. Explore build files, layout, entry points, data layer, external calls. Read `README.md` as a source but verify it against the code.
2. Draft `ARCHITECTURE.md` ([reference/architecture-template.md](reference/architecture-template.md)) describing the system as it *is*.
3. Surface questionable parts (dead seams, inconsistent patterns, risky deps) as findings — don't discard working decisions.
4. Confirm with the user, then write `ARCHITECTURE.md`, including a `Rules and Conventions` section for the patterns the code already follows.
5. If README restates structure, slim it to a pointer to `ARCHITECTURE.md`.


## Wire CLAUDE.md / AGENTS.md

Ensure both exist as thin pointers — never copy bulk in. Keep their existing style if present:

```markdown
# Project context
Read `./ARCHITECTURE.md` for components, stacks, layout, and conventions.
Read `./README.md` for the overview, `./ADR.md` for decision history.
```

## Done

Report which file was created vs. adopted and the next step (`forge spec <first feature>`). A few lines.
