---
name: spec
description: Use before building any non-trivial software change — a feature, service, API, data model, schema, behavior change, or refactor — to turn an intent into a self-contained, build-ready solution spec through collaborative dialogue. Analyse the problem, capture requirements, explore the codebase, decide the approach, and emit verifiable acceptance criteria.
---

Turn an idea into a build-ready solution spec through natural collaborative dialogue: understand the project context, refine the intent one question at a time, weigh approaches, define acceptance criteria, confirm.

A session between user and agent:
| User (Human) | Agent (You) |
|---|---|
| Formulates the task, need or a problem. | Comprehends the request, explores the codebase, asks clarifying questions, challenges assumptions, raises issues/inconsistencies/gaps, suggests solution options — including non-obvious ones the user may not have considered — and surfaces trade-offs. |
| Makes decisions and clarifications.   Validates the suggested appoach | Writes a self-contained solution specification with clear acceptance criteria. |


The spec is the deliverable, not code: don't implement during a spec session — it ends only at a spec the user has confirmed.

Once it's ready, the build is just execution against it — via `/goal` ("work until the acceptance criteria and Definition of Done pass"), a dispatched subagent, or any agent.

The discipline that governs the build lives in `ARCHITECTURE.md` (planted by `arch`), not here.

## Pre-requisites (non-optional)

These are hard prerequisites for producing a valid spec. If one fails, explain the blocker clearly and stop. Do not synthesize missing project context from the prompt.

| Gate | To do if fail |
|---|---|
| `PRODUCT.md` exists and not placeholder | Ask the user to run `prod` (or `/impeccable teach` for design-led projects). Never synthesize it from the prompt. |
| `ARCHITECTURE.md` exists and is substantive (components, stack, conventions). | Ask the user to run `arch`. |

Read `PRODUCT.md`, `ARCHITECTURE.md`, the decision log (`ADR.md`/`DECISIONS.md`), and `IDEAS.md` before the session. Also check variants like `docs/product.md`, `docs/architecture.md`, and `docs/adr/*` only to detect duplicates or source material; `spec` relies on the root `PRODUCT.md` and `ARCHITECTURE.md`. Don't re-read if already loaded this session.

## Match the depth to the problem

Scale the session to the request. A focused, low-risk change earns a couple of sentences and a single confirmation; a nuanced or risky one earns real exploration — alternatives, trade-offs, a sketch. Don't impose heavy elaboration where the problem doesn't call for it, when unclear - ask before elaborating.

## 1. Explore project context

Understand the ground you're building on:
- Read `PRODUCT.md`, `ARCHITECTURE.md`, `IDEAS.md`, and the decision log (`ADR.md`/`DECISIONS.md`)
- Check files, docs and recent commits
- Understand layers and components boundaries

## 2. Frame the problem

- **Understand the problem.** If the request is a proposed solution - establish the motivation - why it matters.
- Transform vague requests into concrete goals.
- **State assumptions** and verify the risky ones; don't build against an unvalidated one.
- **Right-size** If the request spans several independent subsystems, or assumes too many changes, confirm if the user wants to split it and suggest options.

- **Gap analysis** — what's ambiguous, missing, or contradictory; only what blocks building.

## 3. Design solution

- **Explore alternatives, don't anchor.** When the problem warrants it, generate 2-3 genuinely different approaches — include one simpler, and one non-obvious option if you see it. Present the forks conversationally via `AskUserQuestion`, recommend one, and say why it beats the others.
- Ask one thing at a time, don't ask what you can verify. Push back when warranted.
- YAGNI: Remove what the core value doesn't need, name what's out, and defer non-essential ideas to `IDEAS.md`.
- If the existing code has smells/problems in the path of the change (a file grown too large, tangled responsibilities, unclear boundaries), fold targeted fixes into the spec — the way a good engineer improves the code they touch. But don't propose unrelated refactoring; stay on the goal.
- If the feature forces a system-level change (new component, boundary shift, data model change, or a new dependency), flag it as the architecture update that need to be put in the changelog.
- Avoid duplications and restatements of `PRODUCT.md`/`ARCHITECTURE.md` - link instead.
- **Be concrete.** Favor artifacts — trees, schemas, signatures — over prose that restates them. Foundational contracts as real/pseudo code belong in the spec; full implementations don't. (The template defines the blocks and their formats.)
- **Capture decisions inline** as you settle them; don't write `ADR.md`/`IDEAS.md` during the session — the build propagates them.
- **A refactor is governed by TDD:** establish a green safety net (characterization tests first if coverage is thin) before restructuring; the criterion is behavior preserved, not new behavior.
- **The acceptance criteria** are the linchpin — phrase them as checkable conditions; they become the build's stop-condition.
- **The Definition of Done** travels in every spec as the build's quality gate; fill its test command for real, not a placeholder. (The template carries the DoD items.)
- **Status lifecycle:** `spec` sets `Draft` → `Ready to build`; the build flips it to `Done`. A scan of `Status:` lines across `docs/specs/` is the progress trail — no separate file.

## 4. Present and confirm the solution

Don't just dump a spec with the details buried in it; present the chosen solution clearly in a way easy to grasp for a human:
- Visualize with ASCII sketch if it helps.
- Highlight components affected by the planned changes.
- Obtain confirmation that the spec captures the intent and is ready to build. If not, iterate.

## 5. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`nnn` = next sequence for the date; `<slug>` = kebab feature name).

Decisions live **inline** in the spec's *Decisions* section in the format from [reference/decisions.md](reference/decisions.md); the build propagates them to `ADR.md` and deferred ideas to `IDEAS.md` as part of the DoD — don't write the logs during the session.

## Quality checklist

Self-review the spec with fresh eyes before declaring it ready:
- [ ] The spec should be minimal but sufficient to build from cold (on empty context).
- [ ] The acceptance criteria should be verifiable, to be directly used as `/goal` stop-conditions.
- [ ] The DoD's test command is real, not a placeholder.
- [ ] Scope fits a single build — or was split with the user.
- [ ] A refactor has a green safety net established before restructuring.
- [ ] Decisions are inlined, not pre-written to the log.
- [ ] No full implementations or step-by-step task lists; no duplications.
- [ ] No contradictions between sections (e.g. scope vs. acceptance criteria).
- [ ] No requirement that reads two ways
- [ ] No placeholders/TBD

**When done:**
- confirm the spec path
- commit the spec
- report it's ready to execute and give the one-line `/goal` (or subagent brief) as the next step that builds it. A few lines, no narrative.


