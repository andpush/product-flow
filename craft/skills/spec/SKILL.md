---
name: spec
description: Must be used when asked to build any non-trivial changes to the software — a feature, service, API, data model, schema, behavior change, or refactoring — to analyse user intent, discover requirements, brainstorm and plan the approach.
---

Turn an intent into a self-contained, build-ready solution spec through collaborative dialogue. The spec is a handout for a build agent, so it must be clear and concrete enough to execute from cold, without further clarifications or design decisions.

During this collaborative session: understand context -> refine intent -> discover hidden decisions and surface tradeoffs -> define the approach -> define acceptance criteria, confirm readiness for delegated build.

A session between user and agent:
| User (Human) | Agent (You) |
|---|---|
| Formulates the task, need or a problem. Provides guidance, clarifications and explanations.| Comprehends the request, explores the codebase, asks clarifying questions, challenges assumptions, raises issues/inconsistencies/gaps, suggests solution options — including non-obvious ones the user may not have considered — and surfaces trade-offs. |
| Makes informed decisions and clarifications. Validates the suggested approach. | Writes a self-contained solution specification with clear acceptance criteria. |


The spec is the deliverable, not code: don't implement during a spec session — it ends only at a spec the user has confirmed.

Once it's ready, the implementation is a delegated execution — via `/goal`, a dispatched subagent, or any agent.

## Context gates — detect, don't dead-end

`spec` builds on `PRODUCT.md` and `ARCHITECTURE.md`. Map them first (and variants — `docs/product.md`, casing) so existing context isn't missed.

If either is missing or placeholder-only, don't wall off — offer a fork:
- **Establish now** — run `prod`/`arch` in this session, scaled to the request (a quick minimal doc for a small change; full discovery for a new project), then continue the spec.
- **Defer** — name what's missing and why it matters, then stop so the user runs `/prod`/`/arch` separately.

Never synthesize `PRODUCT.md`/`ARCHITECTURE.md` from the prompt — the offer is to establish them properly, not fabricate.

## Core Principles

### Match the depth to the problem

Scale the session to the request. A focused, low-risk change earns a couple of sentences and a single confirmation; a nuanced or risky one earns real exploration — alternatives, trade-offs, a sketch. Don't impose heavy elaboration where the problem doesn't call for it, when unclear - ask before elaborating.

### User interaction

Proactively involve user in the discovery: you get precious information, they gain direction and can steer.

Speak as a professional collaborator: you are tech lead, user is busy domain expert. Value their time, be terse, pragmatic, ask only what affects the solution. Ask questions as they arise; skip Q&A theatre. Push back when warranted.

## Process

### 1. Explore the context
Understand the ground you're building on:
- Read `PRODUCT.md`, `ARCHITECTURE.md`.
- Peek into dir tree, recent commit log, `IDEAS.md`, `ADR.md` if warranted.
- Explore additional context and zoom in as needed.

### 2. Frame the problem

In touch with user, turn vague requests into concrete goals. Grasp the problem, not just gather requirements. If the request is a proposed solution, establish the motivation. Verify risky assumptions. Challenge contradictions and gaps. Push for clarity on the core value and the acceptance criteria.

If the request spans several independent subsystems, or assumes too many changes, confirm if the user wants to split it and suggest options.

### 3. Design the solution

Define the approach. Start simple, surface trade-offs, involve the user.

As new information arises, iterate between the solution and the problem framing — they shape each other. Refer to the codebase when context required.

If the problem warrants it, generate 2-3 genuinely different approaches — include one simpler, and one non-obvious option if useful. Recommend one and say why it beats the others.

When the change touches them, surface the decisions that cause expensive rewrites — data ownership / source of truth, state and lifecycle rules, boundaries, contracts — while they're still cheap to change; don't let them first surface in the written spec.

Follow defined rules and conventions.

### 4. Write the spec

- Use template [reference/spec-template.md](reference/spec-template.md).
- Lead with the **Review Brief**: the scannable decision surface a human approves from. Keep execution detail below it, and only where it's needed.
- Be concrete, avoid prose, duplications, restatements of `PRODUCT.md`/`ARCHITECTURE.md` - link instead.
- YAGNI: Focus on the core value, and defer non-essential ideas to `IDEAS.md`.
- If the change path crosses code smells (oversized file, tangled responsibilities, unclear boundaries), fold targeted fixes into the spec — improve what you touch. Don't propose unrelated refactoring.
- Flag architectural impact when the feature forces a system-level change: new component, boundary shift, data model change, or new dependency.
- Define a feature-relevant testing approach following the testing pyramid. For UI changes, consider e2e (Playwright or similar). Gate refactoring with TDD: establish a green safety net before restructuring.
- Acceptance criteria are the implementation agent's stop condition. Minimum: code builds and runs, no lint errors, tests green, behavior change observable. Add criteria where needed to pin down intent.

### 5. Present and confirm

Don't just dump a spec with the details buried in it; present the chosen solution clearly in a way easy to grasp for a human:
- Visualize with ASCII sketch if it helps.
- Highlight components affected by the planned changes.
- Obtain confirmation that the spec captures the intent and is ready to build. If not, iterate.

### 6. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`nnn` = next sequence for the date; `<slug>` = kebab feature name).


## `IDEAS.md` entry format

```markdown
- [ ] YYYY-MM-DD · [area] — the idea in one line (why it might matter).
```


## Quality checklist

Self-review the spec with fresh eyes before declaring it ready:
- [ ] The spec should be minimal but sufficient to implement from cold (on empty context)
- [ ] The Review Brief lets a human approve the approach without reading the execution detail
- [ ] The acceptance criteria should be verifiable
- [ ] Testing approach is defined
- [ ] No full implementations or step-by-step task lists; no duplications
- [ ] No contradictions between sections (e.g. scope vs. acceptance criteria)
- [ ] No requirement that reads two ways

## When done

- confirm the spec path
- if no open blockers - set status `Ready to build`, otherwise `Draft`
- commit the spec
- report it's ready to execute and give the one-line `/goal` (or subagent brief) as the next step that builds it. A few lines, no narrative.
