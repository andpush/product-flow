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

For visual/UI/UX work use `impeccable` instead, not forge.

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

Raise architecture/feasibility questions from what you found. If the feature forces a system-level change (new component, boundary shift, data model change, or a new dependency), flag it as a `forge teach` update — don't bake it into the spec.

## 2. Frame the problem, then decide

- **Problem before solution.** The request is usually a proposed solution. Establish the underlying problem — who has it, why it matters — and sanity-check it's real before designing. State assumptions explicitly and verify the risky ones; don't build against an unvalidated one.
- **Decompose if too big.** If the request spans several independent subsystems, say so and split it — each piece gets its own spec. Don't refine details of something that needs decomposing first.
- **Gap analysis** — what's ambiguous, missing, or contradictory; only what blocks building.
- **Explore alternatives, don't anchor.** Generate 2-3 genuinely different approaches before settling, and include one simpler than your first instinct — the first idea and the familiar pattern aren't automatically right. Present the real forks as **pro/contra** via `AskUserQuestion`, recommend one, and say why it beats the others.
- Apply the project's standing decision rule from `ARCHITECTURE.md`: surface the trade-off, prefer the simpler option, challenge a weak default — then move. No paralysis. Ask one thing at a time; don't ask what you can verify.
- Keep scope honest: name what's out, defer non-essential ideas to `IDEAS.md`.

Record significant decisions tersely in the project's decision log — see [reference/decisions.md](reference/decisions.md).

## 3. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`nnn` = next sequence for the date; `<slug>` = kebab feature name).

Record what's expensive or risky to recover, not what's cheap to look up: intent, decisions, files/patterns to reuse, scope, test approach, and **verifiable acceptance criteria**. Exclude generated code, step-by-step task lists, and restatements of `PRODUCT.md`/`ARCHITECTURE.md` (link instead).

The acceptance criteria are the linchpin: phrase them as checkable conditions so they can serve directly as a `/goal` stop-condition. Vague criteria make execution flail.

## Done

Self-review the spec with fresh eyes before declaring it ready: no placeholders/TBD, no sections that contradict each other, scope fits a single build, and no requirement that reads two ways (pick one, make it explicit). Fix inline.

Then confirm the spec path and any open items the human must still resolve. If none remain, say it's ready to execute and give the one-line `/goal` (or subagent brief) that builds it. A few lines, no narrative.
