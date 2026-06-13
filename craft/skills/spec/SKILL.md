---
name: spec
description: Must be used when asked to build any non-trivial changes to the software — a feature, service, API, data model, schema, behavior change, or refactoring — to analyse user intent, discover requirements, brainstorm and plan the approach.
---

Turn an intent into a self-contained, build-ready solution spec through collaborative dialogue. The spec is a handoff for a build agent, so it must be clear and concrete enough to execute from cold, without further clarifications or design decisions.

During this collaborative session: understand context -> refine intent -> discover hidden decisions and surface tradeoffs -> define the approach -> define acceptance criteria, confirm readiness for delegated build.

A session between user and agent:
| User (Human) | Agent (You) |
|---|---|
| Formulates the task, need or a problem. Provides guidance, clarifications and explanations.| Comprehends the request, explores the codebase, asks clarifying questions, challenges assumptions, raises issues/inconsistencies/gaps, suggests solution options — including non-obvious ones the user may not have considered — and surfaces trade-offs. |
| Makes informed decisions and clarifications. Validates the suggested approach. | Writes a self-contained solution specification with clear acceptance criteria. |


The spec is the deliverable, not code: don't implement during a spec session — it ends only at a spec the user has confirmed.

Once it's ready, the implementation is a delegated execution — via `/goal`, a dispatched subagent, or any agent.

## Context gates — detect, don't dead-end

`spec` builds on `PRODUCT.md` and `ARCHITECTURE.md`.

If either is missing or placeholder-only — offer a fork:
- **Establish now** — run `prod`/`arch` skills in this session, then continue the spec.
- **Defer** — name what's missing and why it matters, then stop so the user runs `/init` separately.

## Core Principles

### Match the depth to the problem

Scale the session to the request. A focused, low-risk change earns a couple of sentences and a single confirmation; a nuanced or risky one earns real exploration — alternatives, trade-offs, a sketch.

### Lead the conversation

Proactively involve user, drive the discovery: doing so you get precious information, they gain direction and can steer.

Speak as a professional collaborator: you are tech lead, user is domain expert. You guide to reach consensus and shape the best solution.

Be terse, pragmatic, ask only what affects the solution, no Q&A theatre. That means fewer, sharper exchanges, not skipping the dialogue to write faster. Follow this pattern:
- Open by reflecting the problem back in your own words, then ask the sharpest unknown. Make the user react and correct, not author from scratch.
- Pursue one thread before opening the next. A dialogue beats a questionnaire. Top-down: Start each topic with summary that validates shared common ground, then move to details. Each answer should sharpen your next question.
- Challenge. Name the assumption you think is shaky, the contradiction you spotted, the simpler path they may not have considered — and say what you'd do and why. Bring a recommendation to every fork; make the user approve or override, not decide in a vacuum.
- Surface the non-obvious. Part of your value is raising what the user didn't think to ask — edge cases, failure modes, cheap-now/expensive-later decisions.
- Earn the right to write. Summarize and write back to ensure you got it right, and get the nod before writing.

## Process

### 1. Explore the context
Understand the ground you're building on:
- Read `PRODUCT.md`, `ARCHITECTURE.md`.
- Peek into dir tree, recent commit log, `docs/ideas/` and `docs/adr/` listings if warranted.
- Explore additional context and zoom in as needed.

### 2. Frame the problem

In touch with user, turn vague requests into concrete goals. Grasp the problem, not just gather requirements. If the request is a proposed solution, establish the motivation. Verify risky assumptions. Challenge contradictions and gaps. Push for clarity on the core value and the acceptance criteria.

If the request originates as an idea (picked from `docs/ideas/` or a fresh hunch), validate it before specing: does it serve `PRODUCT.md`, is it worth doing now? Recommend a verdict — **pursue**, **defer**, or **reject** — rejection is a legitimate outcome, not a failure. Record the verdict in the idea file (see Ideas below).

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
- YAGNI: Focus on the core value, and defer non-essential ideas to `docs/ideas/`.
- If the change path crosses code smells (oversized file, tangled responsibilities, unclear boundaries), fold targeted fixes into the spec — improve what you touch. Don't propose unrelated refactoring.
- Flag architectural impact when the feature forces a system-level change: new component, boundary shift, data model change, or new dependency.
- Define a feature-relevant testing approach following the testing pyramid. For UI changes, consider e2e using playwright-cli skill or similar. Gate refactoring with TDD: establish a green safety net before restructuring.
- Acceptance criteria are the implementation agent's stop condition. Minimum: code builds and runs, no lint errors, tests green, behavior change observable. Add criteria where needed to pin down intent.

### 5. Present and confirm

Don't just dump a spec with the details buried in it; present the chosen solution clearly in a way easy to grasp for a human:
- Lead the presentation with the diagram — it's the fastest way for a human to grasp and steer the solution.
- Highlight components affected by the planned changes.
- Obtain confirmation that the spec captures the intent and is ready to build. If not, iterate.

### 6. Emit the spec

Write `docs/specs/YYYY-MM-DD-<slug>.md` using [reference/spec-template.md](reference/spec-template.md) (`<slug>` = kebab feature name). If one spec splits into an ordered sequence, insert a letter: `YYYY-MM-DD-A-<slug>.md`, `YYYY-MM-DD-B-<slug>.md`, …


## Ideas

`docs/ideas/` holds one file per idea — candidates, not commitments, never a to-do list. Format and lifecycle are owned by the `idea` skill ([../idea/SKILL.md](../idea/SKILL.md)); filenames are the index — scan with a directory listing, open a file only on pickup. On validation (see Frame the problem), record the verdict in the idea's frontmatter: set `status:` (**pursued** → add `spec:` path, **deferred**, or **rejected** — keep the file), put the one-line rationale in `verdict:`, bump `updated`. On a terminal status (**pursued**/**rejected**) move the idea file and any same-basename images into `docs/ideas/done/` (`git mv` when tracked); **deferred** stays at top level. Don't open a spec for an unvalidated idea; deleting idea files is the user's call, never yours.


## Quality checklist

Self-review the spec with fresh eyes before declaring it ready:
- [ ] The spec is minimal but sufficient to implement from cold (on empty context)
- [ ] The acceptance criteria is verifiable
- [ ] Testing approach is defined
- [ ] No contradictions between sections (e.g. scope vs. acceptance criteria)
- [ ] No requirement that reads two ways

## When done

- if no open blockers - set `status: ready` and commit, otherwise `status: draft`
- report it's ready to execute and give the one-line `/goal` (or subagent brief) as the next step that builds it. A few lines, no narrative.

Once the build lands and the spec reaches `status: done`, archive it: move the spec file and any same-basename images into `docs/specs/done/` (`git mv` when tracked, `mkdir -p` if absent). Top-level `docs/specs/` stays the live set; `done/` is the archive.
