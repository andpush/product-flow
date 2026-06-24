# Product Flow

Product development workflow for agentic development. From idea to production.

This repo ships one plugin: **`craft`** — a lightweight SDD workflow: **prod** → **arch** → **spec** → **build** for:

- guided discovery
- visible decisions
- active conversational steering
- delegated generation
- minimum burnt tokens: no detailed planning unless it changes the outcome

Make expensive decisions visible early: product, architecture, feature design. Capture them in
durable, scannable files so build becomes execution against a clear spec.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install craft
```

It is also recommended to have these skills configured:
    - simplify
    - code-review
    - playwright-cli

## Workflow

You delegate the coding, not the decisions. Fast generation hides early mistakes — wrong data model, accidental boundaries. Craft surfaces expensive-to-undo decisions while they're cheap to change, recommends, lets you steer. Token-frugal: no planning that doesn't change the outcome, no questionnaire theatre.

Core flow: `prod` → `arch` → `spec` → build. Alongside:

1. Call `prod` to collaboratively create (or update) `PRODUCT.md` that is required for further steps. One time, so prefer bigger models/thinking efforts, e.g. Opus/high.
2. Call `arch` to collaboratively create (or update) `ARCHITECTURE.md` that is required for further steps. One time, so prefer bigger models/thinking efforts, e.g. Opus/high.
3. Call `spec` to collaboratively create a solution spec that is ready for the execution. Prefer medium models/efforts combinations: Opus/medium, GPT-5.5.
4. Use built-in `/goal` command in a new/clean session to implement the spec till completion. You can use faster/cheaper models here (Sonnet, GLM-5.2, Minimax M3). This session usually can work unattended or in a headless subagent as long as permissions are granted or auto mode is on.

Each skill works greenfield (define with you) or brownfield (derive from existing code, then confirm),
and adopts existing files rather than clobbering them.

```text
prod → arch → spec → build (/goal, a subagent, or any agent)
```

Optionally you can run `simplify` or `review` skill (not included, use from any vendor you trust) in a clear context to ensure code quality and reuse. Having context cleared helps remove creator bias, using a different model (e.g. GPT-5.5) helps as well.

## Skills

| Skill | Produces |
| --- | --- |
| `prod` | `PRODUCT.md` — purpose, users, value, constraints, MVP scope |
| `arch` | `ARCHITECTURE.md` — components, stack, boundaries, conventions |
| `spec` | `docs/specs/*.md` — one buildable feature spec with verifiable acceptance criteria (archived to `docs/specs/done/` once `done`) |
| `next` | `docs/next/*.md` — terse handoff doc for a small, ready-to-execute task (usually one component, no architecture work); archived to `docs/next/done/` once `done` |
| `idea` | `docs/ideas/*.md` — one-file idea capture with a quick PRODUCT.md alignment check |
| `audit` | `docs/audit-YYYY-MM-DD.md` — deep repo health check: structure, maintainability, security |
| `doc-refactor` | normalized document — merge, deduplicate, and restructure docs while preserving relevant knowledge |
| `whereami` | report — reorient after a break: current focus, parked ideas, next step |
| `ba` | business analysis and requirements decomposition |
| `sa` | software architecture design |
| `code-explorer` | codebase exploration and understanding |
| `code-reviewer` | code quality review and improvements |
| `compare` | comparison of two codebases, with a winner |
| `slides` | presentation decks from markdown |
| `ui-mockup` | clickable HTML mockups from product specs |
| `uiux-design` | UI/UX design |

## Usage

Invoke the skills by name in your agent host:

```text
/craft:init      # small project: run prod then arch in one scaled-down session
/prod            # define the product with user
/arch            # define the architecture with user
/spec <feature>  # frame a feature into a spec with user
/next <task>     # frame a small task into a terse handoff doc in docs/next/
/idea <hunch>    # capture an idea into docs/ideas/, checked against PRODUCT.md
/audit           # deep repo health check; writes docs/audit-YYYY-MM-DD.md
/doc-refactor <inputs> -> <output> [goal] # merge, dedupe, and restructure docs
/whereami        # reorient: current focus, parked ideas, next step
/clear           # clear context
/goal <spec_file> # work on spec till done - unattended.
```

`/craft:init` is a convenience macro for small/fresh projects — it just chains `prod` then `arch`.
For larger or evolving projects, run `/prod` and `/arch` separately so each can be revisited on its own.

## Well known files

| File | Holds | Created by |
|---|---|---|
| `PRODUCT.md` | purpose, users, constraints | `prod` (or `/impeccable teach`) |
| `ARCHITECTURE.md` | components, stacks, boundaries, layout, entrypoints, conventions | `arch` skill or manually |
| `docs/specs/*.md` | one buildable feature spec each — live at top level, `done` files move to `docs/specs/done/` | `spec` skill or manually |
| `docs/next/*.md` | small ready-to-execute tasks, one file each — `status: todo` while live, `done` files move to `docs/next/done/`; delete a file to drop a task | `next` skill or manually |
| `docs/adr/*.md` | why choices were made, one decision per file | `arch`/`spec` skills, over time |
| `docs/ideas/*.md` | idea backlog, one file per idea (images beside) — unvalidated candidates, not commitments; optional `priority: high\|low` steers `whereami`; `spec` validates on pickup (pursue / defer / reject); closed ideas move to `docs/ideas/done/`; delete a file to drop an idea | `idea` skill or manually |
| `docs/audit-YYYY-MM-DD.md` | repo health snapshot — findings, quality scores, action items | `audit` skill |
| `README.md` | human onboarding | human; read as a source |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | `arch` skill or manually |

Memory is scannable files, not prose — one file per spec/idea/decision, filenames are the index.

Closed work is archived, not deleted: when a spec or next-task reaches `done` or an idea is
`pursued`/`rejected`, its file (and any images) move into a `done/` subfolder — `docs/specs/done/`,
`docs/next/done/`, `docs/ideas/done/` — so top-level stays the live set. `/whereami` flags any closed
file still sitting at top level and suggests the `git mv`.

## Deprecated: staged commands

> **Deprecated.** The staged `/1`–`/9` commands are kept for now but will be removed. Prefer the skills workflow above (`prod` → `arch` → `spec` → build).

The plugin still ships a heavier, staged command flow:

```text
/1-define-product → /2-mockup-product
        │
        ├─ /3-define-architecture
        └─ /4-add-mvp-features → /5-add-feature
                                      │
                                      ├─ /6-mockup-feature
                                      ├─ /7-plan-feature
                                      ├─ /8-implement-feature
                                      └─ /9-review-feature
```

These read input from `docs/` and write artifacts (`PRODUCT.md`, `ARCHITECTURE.md`, `mockups/`, `features/F001-*/`) to the project root.

## License

MIT
</content>
