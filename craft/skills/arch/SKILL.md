---
name: arch
description: Use to define or derive project architecture, stack, and conventions - into a durable ARCHITECTURE.md that the `spec` skill can rely on.
---

Establish the durable engineering context for a software project — architecture, component/module map, tech stack, and coding conventions — either by defining them with the user (greenfield) or deriving them from existing code (brownfield), and wiring CLAUDE.md/AGENTS.md as thin pointers.

Run once; again only when foundations change.

Consumes `PRODUCT.md` (from `prod`); produces `ARCHITECTURE.md`, which `spec` consumes. The design counterpart is the impeccable plugin (https://impeccable.style) — it owns the product's visual/UX design (DESIGN.md); `arch` owns the engineering architecture. Both apply to a project that has a UI.

## Well known files

| File | Holds | Created by |
|---|---|---|
| `PRODUCT.md` | purpose, users, constraints | `prod` (or `/impeccable teach`) |
| `ARCHITECTURE.md` | components, stacks, boundaries, layout, entrypoints, conventions |  this `arch` skill or manually |
| `ADR.md` \| `DECISIONS.md` | why choices were made | appended over time |
| `IDEAS.md` | parked ideas, future scope, items needing elaboration | appended over time |
| `README.md` | human onboarding | human; read as a source |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | this `arch` skill or manually |

## Detect first

Map the well-known files above before creating any, plus variants like `docs/product.md`, `docs/architecture.md`, and `docs/adr/*`. Craft's durable files are `PRODUCT.md` and `ARCHITECTURE.md`: use variants as source material to avoid losing context, and mention any duplicate/refactoring decision to the user. If the repo already keeps conventions in their own file (`rules*.md`, `CONVENTIONS.md`), reference them from `ARCHITECTURE.md` instead of restating.

## Product gate

`arch` requires a substantive `PRODUCT.md`, which provides high level context on WHAT we build. If it is missing or placeholder-only, stop and ask the user to run `prod` first, or use external tool like `impeccable teach` or create manually. Do not invent product purpose, users, or constraints from architecture preferences alone.

## Greenfield: define with the user

1. **Read context.** `PRODUCT.md` for purpose, users, constraints.

2. **Propose architecture and stack.**
   - **Start simple.** KISS, YAGNI. Complexity matched to the problem.
   - **Important:** Architecture and stack shape each other — iterate to coherence: propose components with preliminary tech, validate the tech against the components, refine both.
   - **Explore alternatives.** Present substantial forks: 2-3 options and recommend one via `AskUserQuestion`. Don't bikeshed settled defaults; riskier decisions are closer to data and API boundaries. Examples: monolith vs. services, pre-built vs. bespoke, paid vs. open-source, concurrent vs. sequential, relational vs. object, message queue vs database, persistent vs. in-memory, etc.

3. **Write `ARCHITECTURE.md`** using [reference/architecture-template.md](reference/architecture-template.md).

4. **Seed `Rules and Conventions`** from [reference/conventions-seed.md](reference/conventions-seed.md). Take only the sections that fit the chosen stack, adapt with the user, keep only the non-obvious or project-specific.


## Brownfield: derive from the code, then confirm

1. Explore build files, layout, entry points, data layer, external calls. Read `README.md` as a source but verify it against the code.
2. Draft `ARCHITECTURE.md` ([reference/architecture-template.md](reference/architecture-template.md)) describing the system as it is.
3. Surface questionable parts as findings — don't discard working decisions. Suggest parking improvements in `IDEAS.md`.
4. Confirm with the user, then write `ARCHITECTURE.md`, including a `Rules and Conventions` section for the patterns and practices the code already follows.
5. If README restates structure, slim it to a pointer to `ARCHITECTURE.md`.

## Architecture quality checklist

Apply when drawing or revisiting component boundaries:
- [ ] **Acyclic dependencies.** Keep the component dependency graph acyclic — if two components depend on each other, resolve it (merge, extract a shared piece, or invert a dependency).
- [ ] **Boundaries clarity.** For each unit you should be able to say what it does, how it's used, and what it depends on. Can someone grasp it without reading its internals, and can its internals change without breaking consumers? If not, the boundaries need rework.

## Wire CLAUDE.md / AGENTS.md

Ensure both exist as thin pointers — never copy bulk in. Keep their existing style if present:

```markdown
# Project context
Read `PRODUCT.md`, `ARCHITECTURE.md` for durable context.
When needed, peek into:
- `README.md` for onboarding;
- `IDEAS.md` for parked thoughts;
- `ADR.md`/`DECISIONS.md`for decision history.
```

## Done

Report whether `ARCHITECTURE.md` was created vs. adopted and the next step (`spec <first feature>`). A few lines.
