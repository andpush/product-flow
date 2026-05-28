# Craft Memorandum

Craft is an SDD plugin for people who want to stay top-level decision makers: product owners, directors, CTOs.

For those who want agents to reduce coding effort, not control.

The split:

- agent: explore, analyze, propose, implement, test, review, update memory
- human: steer intent, reveal motivation, choose tradeoffs, approve important decisions

Craft makes this split operational: from guided discovery to delegated coding.

## Problem

Fast generation hides early mistakes.

The first pass may look good while the data model is wrong, boundaries are accidental, ownership is unclear, tests are shallow, and future maintenance cost is already baked in.

The model may not see the debt. The user may see it only after more features make rewrite cheaper than repair.

Craft targets this failure: make bad foundations visible before they become code.

More specs are not the goal. Earlier decision visibility is.

## Differentiator

Craft differs by four constraints:

- guided conversational discovery
- visible decisions without cognitive overload
- delegated generation after human judgment
- minimum burnt tokens: no detailed planning unless it changes the outcome

Craft turns intent into visible decisions, then into delegated execution.

The agent explores, finds hidden decisions, surfaces them while cheap to change, and lets the user steer.

Conversation is discovery, not questionnaire:

- "I found this constraint."
- "It implies two designs."
- "I recommend this because ownership stays clear."
- "The faster option makes this future feature harder."
- "Which tradeoff matches your intent?"

Ask when discovered. Ask only what changes the solution.

## Visible Decisions

Craft must expose decisions that cause expensive rewrites:

- data model and ownership
- component boundaries
- source of truth
- API contracts
- persistence and migration strategy
- state and lifecycle rules
- dependency choices
- UX flows that affect architecture
- test strategy and safety net
- scope cuts and deferred ideas

Silent decision means failure.

Decision first seen in the finished spec means late discovery.

## Product

`prod` captures what constrains future decisions:

- who has the problem
- which problem matters
- intended solution direction
- value to preserve
- in scope
- out of scope
- hard constraints
- success signals

It is not a roadmap, pitch, or marketing brief.

It prevents agents from treating every task as local code work.

## Architecture

`arch` captures the engineering map for future decisions.

Not an encyclopedia. A review surface.

It should show:

- components and responsibilities
- ownership boundaries
- data ownership and core entities
- component communication
- entrypoints and commands
- non-obvious conventions
- important risks and decisions

Visuals matter when they reveal structure: system boundaries, data model, flow, state, ownership.

Diagrams are review tools, not decoration. They let the user catch wrong foundations before code multiplies them.

The template is a checklist. The emitted architecture includes only what matters for this system.

## Spec

`spec` turns intent into a build-ready decision record.

Two jobs:

1. Fast human review.
2. Clear-context agent execution.

Too short hides decisions. Too long buries them.

Required shape:

- review brief first
- execution detail only where needed
- acceptance criteria as stop conditions
- explicit non-goals
- rejected alternatives when they clarify the choice
- data/API/architecture impact when relevant

The spec is synchronized thinking compressed. Not a transcript. Not an essay.

## Memory

Craft memory prevents archaeology:

- `PRODUCT.md` - product intent and constraints
- `ARCHITECTURE.md` - system shape, boundaries, stack, commands, conventions
- `ADR.md` or `DECISIONS.md` - important product and architecture decisions with rationale
- `IDEAS.md` - parked ideas, potential future scope, items needing elaboration

Memory must answer:

- where are we?
- why did we choose this?
- what happens next?

If memory becomes a prose dump, it failed.

## Quality Gate

Delegated coding needs hard stops.

Done means:

- behavior implemented
- tests written
- tests pass
- acceptance criteria met
- no duplication
- no dead code
- no obvious security issue
- no contradiction with decisions
- memory updated
- changes committed

Not "looks done." Verified done.

## Avoid

- architecture hidden in code
- lengthy questionnaires
- accidental data models
- documentation archaeology
- heavy process for tiny tasks
- bikeshedding discussions

## Standard

Craft succeeds when guided discovery creates enough clarity for delegated coding: `/goal`, headless agents, or any executor can implement with zero extra context and no silent redesign.

Goal: maximum leverage, not maximum automation.

Human judgment on decisions. Agent execution after.
