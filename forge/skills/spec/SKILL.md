---
name: spec
description: Use to turn an intent into a buildable spec for a non-UI software feature, service, API, data model, schema, or refactor — capturing requirements, exploring the codebase, deciding architecture/tech-stack and feasibility, and emitting a self-contained spec with verifiable acceptance criteria. The spec is then executed by `/goal`, a subagent, or any agent — this skill does not run the build. For visual/UI/UX work use `impeccable` instead.
---

A working session between you (agent) and the human that turns an intent into a **self-contained spec** a cleared session, a different model, or a headless agent can build from. The human decides; you transfer intent, find gaps, load the coding context, and surface the real trade-offs.

The spec is the deliverable. Once it's ready, the build is just execution against it — via `/goal` ("work until the acceptance criteria pass"), a dispatched subagent, or any agent. The discipline that governs the build lives in `ARCHITECTURE.md` (planted by `forge teach`), not here.

## Setup (non-optional)

| Gate | Check | If fail |
|---|---|---|
| Product | `PRODUCT.md` exists and is substantive (not placeholder, >200 chars). | Run `$impeccable teach` or ask the user to write it. Never synthesize it from the prompt. |
| Context | `ARCHITECTURE.md` exists and is substantive (components, stack, conventions). | Run `forge teach` first. |

Read `PRODUCT.md`, `ARCHITECTURE.md`, the decision log (`ADR.md`/`DECISIONS.md`), and `IDEAS.md` before the session. Don't re-read if already loaded this session.

## 1. Load the coding context first

Take `ARCHITECTURE.md` as given and design *within* it — the per-feature delta, not the whole system.
- Entry points and the modules this target touches.
- Existing functions, utilities, and patterns to **reuse** — name real file paths.
- Data model and external calls involved.
- Feasibility constraints and risks specific to this codebase.

Raise architecture/feasibility questions from what you found. If the feature forces a system-level change (new component, boundary shift, stack addition, or a new dependency edge that would create a cycle between components), flag it as a `forge teach` update — don't bake it into the spec.

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
