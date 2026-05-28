---
name: spec
description: Use when asked to build any non-trivial software change — a feature, service, API, data model, schema, behavior change, or refactor — to analyse the intent, discover requirements , decide and plan the approach.
---

Turn an intent into a self-contained, build-ready solution spec through collaborative dialogue.

During the collaborative session: understand context -> refine intent -> discover hidden decisions and surface tradeoffs -> define the approach -> define acceptance criteria, confirm readiness for delegated build.

A session between user and agent:
| User (Human) | Agent (You) |
|---|---|
| Formulates the task, need or a problem. | Comprehends the request, explores the codebase, asks clarifying questions, challenges assumptions, raises issues/inconsistencies/gaps, suggests solution options — including non-obvious ones the user may not have considered — and surfaces trade-offs. |
| Makes decisions and clarifications. Validates the suggested approach. | Writes a self-contained solution specification with clear acceptance criteria. |


The spec is the deliverable, not code: don't implement during a spec session — it ends only at a spec the user has confirmed.

Once it's ready, the build is delegated execution — via `/goal` ("work until the acceptance criteria and Definition of Done pass"), a dispatched subagent, or any agent.

The spec is ready when another agent can execute it cold, without redesign.

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

## 1. Explore the context
Understand the ground you're building on:
- Read `PRODUCT.md`, `ARCHITECTURE.md`, `IDEAS.md`, decision log (`ADR.md`/`DECISIONS.md`), relevant files, docs, recent commit log.
## 2. Frame the problem
In touch with user, turn vague requests into concrete goals. If the request is a proposed solution, establish the motivation. Verify risky assumptions. Challenge contradictions and gaps. Push for clarity on the core value and the acceptance criteria.
If the request spans several independent subsystems, or assumes too many changes, confirm if the user wants to split it and suggest options.

## 3. Design the solution

Define the approach. If the problem warrants it, generate 2-3 genuinely different approaches — include one simpler, and one non-obvious option if useful. Recommend one and say why it beats the others.

Ask questions when they arise. Don't ask what you can verify or that don't affect the solution. Push back when warranted.

Follow rules and conventions in `ARCHITECTURE.md`.

## 4. Write the spec

- Use template [reference/spec-template.md](reference/spec-template.md).
- Be concrete, avoid prose, duplications, restatements of `PRODUCT.md`/`ARCHITECTURE.md` - link instead.
- YAGNI: Focus on the core value, and defer non-essential ideas to `IDEAS.md`.
- If the existing code has smells/problems in the path of the change (a file grown too large, tangled responsibilities, unclear boundaries), fold targeted fixes into the spec — the way a good engineer improves the code they touch. But don't propose unrelated refactoring; stay on the goal.
- Flag significant architectural changes - in case the feature forces a system-level change (new component, boundary shift, data model change, or a new dependency).


- **A refactor** is governed by TDD: establish a green safety net before restructuring.
- The **acceptance criteria** are the linchpin — phrase them as checkable conditions; they become the build's stop-condition.

## 5. Present and confirm

Don't just dump a spec with the details buried in it; present the chosen solution clearly in a way easy to grasp for a human:
- Visualize with ASCII sketch if it helps.
- Highlight components affected by the planned changes.
- Obtain confirmation that the spec captures the intent and is ready to build. If not, iterate.

## 6. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`nnn` = next sequence for the date; `<slug>` = kebab feature name).


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
- set status `Ready to build`
- commit the spec
- report it's ready to execute and give the one-line `/goal` (or subagent brief) as the next step that builds it. A few lines, no narrative.
