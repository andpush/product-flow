# Product Flow

Product development workflow for agentic development — from idea to production. Ships one plugin,
**`craft`**: a lightweight SDD flow **prod → arch → spec → build**. Discovery is guided and
conversational — craft surfaces expensive-to-undo decisions (data model, boundaries) while they're
cheap to change, recommends, and lets you steer; you delegate the coding, not the decisions.
Token-frugal: no planning that doesn't change the outcome, no questionnaire theatre. Decisions land
in durable, scannable files so build is execution against a clear spec.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install craft
```

Recommended companion skills: `simplify`, `code-review`, `playwright-cli`.

## Workflow

`prod → arch → spec → build`; each skill works greenfield (define with you) or brownfield (derive
from code, then confirm), adopting existing files rather than clobbering them.

1. **`prod`** → `PRODUCT.md`, **`arch`** → `ARCHITECTURE.md`. Required for later steps; one-time, so use bigger models (Opus/high). Or write them by hand / via `/impeccable teach`.
2. **`spec`** → a buildable spec in `docs/specs/`. Medium efforts (Opus/medium, GPT-5.5).
3. **build** — run `/goal <spec>` in a clean session till done; faster/cheaper models (Sonnet, GLM-5.2, Minimax M3), unattended or headless once permissions/auto are granted.

Optionally run `simplify` or `review` (any vendor) in a cleared context to catch quality/reuse
issues — fresh context removes creator bias, a different model (e.g. GPT-5.5) helps more.

## Skills

Invoke by name in your agent host (`/prod`, `/spec <feature>`, …).

| Skill | Does |
| --- | --- |
| `prod` | define the product → `PRODUCT.md` |
| `arch` | define architecture → `ARCHITECTURE.md` |
| `spec <feature>` | frame a feature into a buildable spec with verifiable acceptance criteria |
| `next <task>` | terse handoff for a small task (one component, no architecture work) |
| `idea <hunch>` | one-file capture + `PRODUCT.md` alignment check |
| `audit` | deep repo health check: structure, maintainability, security |
| `doc-refactor <in> -> <out> [goal]` | merge, dedupe, restructure docs, preserving knowledge |
| `whereami` | reorient after a break: focus, parked ideas, next step |
| `init` | macro chaining `prod` then `arch` for a small/fresh project |
| `ba` | requirements decomposition |
| `sa` | architecture design |
| `code-explorer` | explore a repo |
| `code-reviewer` | review code quality |
| `compare` | compare two codebases, with a winner |
| `slides` | decks from markdown |
| `ui-mockup` | clickable HTML mockups |
| `uiux-design` | UI/UX design |

For larger projects run `/prod` and `/arch` separately so each can be revisited; `/craft:init` only
chains them for a quick start.

## Files

One file per spec/idea/decision — filenames are the index, content is scannable, not prose.

| File | Holds | By |
| --- | --- | --- |
| `PRODUCT.md` | purpose, users, value, constraints, MVP scope | `prod` |
| `ARCHITECTURE.md` | components, stack, boundaries, layout, entrypoints, conventions | `arch` |
| `docs/specs/*.md` | one buildable feature spec each | `spec` |
| `docs/next/*.md` | small ready-to-execute tasks, `status: todo` while live | `next` |
| `docs/ideas/*.md` | idea backlog (images beside); unvalidated; optional `priority: high\|low` steers `whereami`; `spec` validates on pickup (pursue/defer/reject) | `idea` |
| `docs/adr/*.md` | why a choice was made, one decision per file | `arch`/`spec`, over time |
| `docs/audit-*.md` | repo health snapshot: findings, scores, action items | `audit` |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | `arch` or manually |
| `README.md` | onboarding for humans; read as a source | human |

Closed work is archived, not deleted: a `done` spec/task or a pursued/rejected idea moves into a
`done/` subfolder (`docs/specs/done/`, etc.), keeping top level the live set; delete a file to drop
it. `/whereami` flags closed files still at top level and suggests the `git mv`.

## Deprecated: staged commands

> The staged `/1`–`/9` commands still ship but will be removed — prefer the skills workflow above.

```text
/1-define-product → /2-mockup-product
        │
        ├─ /3-define-architecture
        └─ /4-add-mvp-features → /5-add-feature
                                      ├─ /6-mockup-feature
                                      ├─ /7-plan-feature
                                      ├─ /8-implement-feature
                                      └─ /9-review-feature
```

They read `docs/` and write `PRODUCT.md`, `ARCHITECTURE.md`, `mockups/`, and `features/F001-*/`.

## License

MIT
</content>
