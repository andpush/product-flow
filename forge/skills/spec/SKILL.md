---
name: spec
description: Use to turn an intent into a solution spec for a software feature, service, API, data model, schema, or refactor. Analyse the problem, Capture requirements, Explore the codebase, Decide architecture and Emit a self-contained solution spec with verifiable acceptance criteria.
---

A session between user and agent:
| User (Human) | Agent (You) |
|---|---|
| Formulates the task, need or a problem. | Comprehends the request, explores the codebase, asks clarifying questions, raises issues/inconsistencies/gaps, suggests solution options, surfaces trade-offs. |
| Makes decisions and clarifications. | Writes a self-contained solution specification with clear acceptance criteria. |


The spec is the deliverable. Once it's ready, the build is just execution against it — via `/goal` ("work until the acceptance criteria pass"), a dispatched subagent, or any agent.

The discipline that governs the build lives in `ARCHITECTURE.md` (planted by `forge teach`), not here.

Pairs with `impeccable`: impeccable owns the visual/UX design (layout, look, mockups), `spec` owns the engineering solution — including for frontend features that have UI.

## Pre-requisites (non-optional)

These are hard prerequisites for producing a valid spec. If one fails, explain the blocker clearly and stop. Do not synthesize missing project context from the prompt.

| Gate | To do if fail |
|---|---|
| `PRODUCT.md` exists and not placeholder | Ask the user to provide it or run `$impeccable teach`. Never synthesize it from the prompt. |
| `ARCHITECTURE.md` exists and is substantive (components, stack, conventions). | Ask the user to run `forge teach`. |

Read `PRODUCT.md`, `ARCHITECTURE.md`, the decision log (`ADR.md`/`DECISIONS.md`), and `IDEAS.md` before the session. Don't re-read if already loaded this session.

## 1. Codebase exploration: understand the ground you're building on

Understand the system as it is before designing the solution. Pay attention to:
- Entry points and the modules this target touches.
- Existing functions, utilities, and patterns to reuse.
- Data model and external calls involved.
- Risks and constraints specific to this codebase.

Raise architecture/feasibility questions from what you found. If the feature forces a system-level change (new component, boundary shift, data model change, or a new dependency), flag it as the architecture update.

## 2. Frame the problem

- **Understand the problem.** The request is usually a proposed solution. Establish the motivation - why it matters. State assumptions and verify the risky ones; don't build against an unvalidated one.
- **Decompose if too big.** If the request spans several independent subsystems, say so and split it — each piece gets its own spec. Don't refine details of something that needs decomposing first.
- **Gap analysis** — what's ambiguous, missing, or contradictory; only what blocks building.

## 3. Design solution

- **Explore alternatives, don't anchor.** Generate 2-3 genuinely different approaches, and include one simpler than your first instinct. Present the real forks as **pro/contra** via `AskUserQuestion`, recommend one, and say why it beats the others.
- Apply the standing decision rule from `ARCHITECTURE.md`. No paralysis; ask one thing at a time, don't ask what you can verify.
- Keep scope honest: name what's out, defer non-essential ideas to `IDEAS.md`.

## 4. Present the solution

- Present the chosen solution clearly in a way easy to grasp for a human. Use an ASCII sketch if it helps. Don't just dump a spec template with the details buried in it; walk through the highlights.
- Emphasize the planned changes
- Obtain confirmation that the spec captures the intent and is ready to build. If not, iterate.

## 5. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`nnn` = next sequence for the date; `<slug>` = kebab feature name).

The spec should be minimal but sufficient to build from cold.

Record what's expensive or risky to recover, not what's cheap to look up: intent, decisions, files/patterns to reuse, scope, test approach, and **verifiable acceptance criteria**. The acceptance criteria are the linchpin: phrase them as checkable conditions so they can serve directly as a `/goal` stop-condition.

Exclude generated code, step-by-step task lists, duplications and restatements of `PRODUCT.md`/`ARCHITECTURE.md` (link instead).

Record significant decisions tersely in the project's decision log — see [reference/decisions.md](reference/decisions.md).


## Done

Self-review the spec with fresh eyes before declaring it ready: no placeholders/TBD, no sections that contradict each other, scope fits a single build, and no requirement that reads two ways (pick one, make it explicit). Fix inline.

Then confirm the spec path and any open items the human must still resolve. If none remain, say it's ready to execute and give the one-line `/goal` (or subagent brief) that builds it. A few lines, no narrative.
