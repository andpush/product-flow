---
name: teach
description: Use once per project to establish the durable engineering context a software project needs — architecture, component/module map, tech stack, and coding conventions — either by defining them with the user (greenfield) or deriving them from existing code (brownfield), and wiring CLAUDE.md/AGENTS.md as thin pointers. Run again only when foundations change. The engineering counterpart to `impeccable teach`; pairs with the `spec` skill, which consumes its output. For visual/UI/UX setup use `impeccable` instead.
---

Establish the durable engineering context for a project so later spec/build work (and any agent, via `/goal` or subagent) inherits it from project files. Run once at the start; again only when foundations change.

## Roles and their homes

Map these five roles to files. Use the repo's existing filenames if present; otherwise the default.

| Role | Holds | Default file | Owner |
|---|---|---|---|
| Product | purpose, users, constraints | `PRODUCT.md` | impeccable — don't author here |
| Architecture | components, stacks, boundaries, layout, entrypoints, **conventions** | `ARCHITECTURE.md` | `teach`'s output |
| Decisions | why choices were made | `ADR.md` \| `DECISIONS.md` | appended over time |
| Front door | human onboarding | `README.md` | human; read as a source |

`ARCHITECTURE.md` is the canonical contract the `spec` skill relies on — it holds the conventions too, in a Conventions section, so there's no separate rules file. Keep each fact in one file; README links to `ARCHITECTURE.md` rather than restating it.

## Detect first

Map roles to existing files before creating any: check casing/variants — `ARCHITECTURE.md` / `docs/architecture.md`, `ADR.md` / `DECISIONS.md` / `docs/adr/*`, plus `README.md`, `PRODUCT.md`, `CLAUDE.md`, `AGENTS.md`. Adopt the repo's names; only fall back to defaults for roles with no home. If the repo already keeps conventions in their own file (`rules*.md`, `CONVENTIONS.md`), adopt it instead of folding.

## Greenfield: define with the user

1. Read `PRODUCT.md` for purpose, users, constraints.
2. Propose architecture and stack — proven over trendy, complexity matched to the problem. Present real forks (monolith vs. services, datastore, etc.) as pro/contra via `AskUserQuestion`; don't bikeshed settled defaults. Architecture and stack shape each other, so iterate to coherence: propose components with preliminary tech, validate the tech against the components, refine both. When drawing boundaries, keep the component dependency graph acyclic — if two components depend on each other, resolve it (merge, extract a shared piece, or invert a dependency).
3. Write `ARCHITECTURE.md` using [reference/architecture-template.md](reference/architecture-template.md).
4. Write the Conventions section of `ARCHITECTURE.md`, using the matching seed in [reference/stacks/](reference/stacks/) as a basis: read it, adapt with the user, keep only conventions that aren't obvious or that this project deviates on. Include the standing decision rule (below).
5. Record macro decisions tersely (`ADR.md`/`DECISIONS.md`: `YYYY-MM-DD · [component] · Decision / Why`, two to four lines).

## Brownfield: derive from the code, then confirm

1. Explore build files, layout, entry points, data layer, external calls. Read `README.md` as a source but verify it against the code.
2. Draft `ARCHITECTURE.md` ([reference/architecture-template.md](reference/architecture-template.md)) describing the system as it *is*.
3. Surface questionable parts (dead seams, inconsistent patterns, risky deps) as findings — don't discard working decisions.
4. Confirm with the user, then write `ARCHITECTURE.md`, including a Conventions section for the patterns the code already follows. If README restates structure, slim it to a pointer to `ARCHITECTURE.md`.

## Conventions

Keep them in a Conventions section of `ARCHITECTURE.md` — only the non-obvious or project-specific ones. For multiple stacks, use a subsection per stack rather than separate files.

Plant this standing rule in that section:

> On any architectural choice: surface the trade-off, prefer the simpler option, challenge a weak
> default, and record the decision in `ADR.md`/`DECISIONS.md`.

## Wire CLAUDE.md / AGENTS.md

Ensure both exist as thin pointers — never copy bulk in. Keep their existing style if present:

```markdown
# Project context
Read `./ARCHITECTURE.md` for components, stacks, layout, and conventions.
Read `./README.md` for the overview, `./ADR.md` for decision history.
```

## Done

Report which role mapped to which file (created vs. adopted) and the next step (`spec <first feature>`). A few lines.
