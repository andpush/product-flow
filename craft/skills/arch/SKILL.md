---
name: arch
description: Use to define or derive project architecture - into a durable `ARCHITECTURE.md` that the `spec` skill can rely on.
---

Establish the durable engineering context for a software project — architecture, component/module map, tech stack, and coding conventions — either by defining them with the user (greenfield) or deriving them from existing code (brownfield).

Produces or updates `ARCHITECTURE.md`, which `spec` consumes. Run once or after foundations change.

## Initial context

Refer to `PRODUCT.md` and root `README.md` for context on WHAT we build. If both are missing or placeholder — offer to **Establish product context now** — run `prod` skill in this session, then continue with `arch`.

Never invent product purpose, users, or constraints from architecture preferences alone.

Map the well-known files. If the repo already contains conventions (e.g. `rules*.md`), reference them from `ARCHITECTURE.md` instead of restating.

Load [reference/architecture-template.md](reference/architecture-template.md) as a guide for the architecture context structure.

## Greenfield: define with the user

1. Understand the product purpose, users, constraints.

2. Propose architecture and stack.
   - **Start simple.** KISS, YAGNI. Complexity matched to the problem.
   - **Important:** Architecture and stack shape each other — iterate to coherence: propose components with preliminary tech, validate the tech against the components, refine both.
   - **Explore alternatives.** Present substantial forks: 2-3 options and recommend one via `AskUserQuestion`. Don't bikeshed settled defaults; riskier decisions are closer to data and API boundaries. Examples: monolith vs. services, pre-built vs. bespoke, paid vs. open-source, concurrent vs. sequential, relational vs. object, message queue vs database, persistent vs. in-memory, etc. Additional indirection, async, data stores are complexity — suggest only if justified.

3. **Write `ARCHITECTURE.md`** in collaboration with the user, link to existing docs instead of restating them.

4. **Seed `Rules and Conventions`** from [reference/conventions-seed.md](reference/conventions-seed.md). Take only the sections that fit the chosen stack, adapt with the user, keep only the non-obvious or project-specific.

## Brownfield: derive from the code, then confirm

1. **Explore the codebase:**
- Orient first (`PRODUCT.md`, `README.md`, layout, config, dir tree);
- Large repo -> fan out `Explore` agents partitioned by territory, each reports its slice along fixed dimensions — purpose, entry points & boundaries, data, external calls, conventions & tests, backed by `file:line` and snippets. Consolidate in the main context
- Small, flat, or tangled repo -> do a single pass yourself, reading code and taking notes.
2. Draft `ARCHITECTURE.md` ([reference/architecture-template.md](reference/architecture-template.md)) describing the system as it is.
3. Never leave an agreed decision unwritten. Surface questionable parts as findings — don't discard working decisions. Suggest parking improvements using `idea` skill.
4. Confirm with the user, then write `ARCHITECTURE.md`, including a `Rules and Conventions` section for the patterns and practices the code already follows.
5. If README restates structure, slim it to a pointer to `ARCHITECTURE.md`.

## Architecture quality checklist

Apply when drawing or revisiting component boundaries:
- [ ] **Acyclic dependencies.** Keep the component dependency graph acyclic — if two components depend on each other, resolve it (merge, extract a shared piece, or invert a dependency).
- [ ] **Boundaries clarity.** For each unit you should be able to say what it does, how it's used, and what it depends on. Can someone grasp it without reading its internals, and can its internals change without breaking consumers? If not, the boundaries need rework.
- [ ] **Data ownership.** Each piece of data should have a clear owner — the component responsible for its integrity and lifecycle. If data is shared, there should be a clear contract for access and modification.


Report whether `ARCHITECTURE.md` was created vs. adopted and the next step (`/spec <first feature>`). A few lines.
