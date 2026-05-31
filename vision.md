# Vision on agentic development - April 2026

As a CTO, director, or a product visioner, I want to play an important role in product development and architectural decisions and less care about the coding. Especially at project start, I want my desicisions not taken for granted but challenged without extremes. I need harness that provide progressive movement towards end result. I believe in tests, review and some of the roles that came from human practices, but not all of them, certain ceremonies should be skipped. Thus, I need good governance support on product definition, architecture, design, tech decisions, testing and review. Would be great to have trace of features and tasks done without extra beaucracy. I want to be able to continue work at any point in time in future without full rework, knowing where I stopped. At the same time I don;t want to dig through the text of generated specs. Having said that, I want to have main architectural decisions explicit and documented.

My goals:
    - To stay the top level decision-maker (CTO / Product Owner)
    - Delegate coding, not important decisions
    - No cognitive overload → only what matters now
    - No archaeology → no digging through specs
    - No loss of ideas → they live elsewhere
    - Zero friction resume → no thinking required to restart

My waypoints:
    - Structured thinking and quality decisions early
    - Challenge on decisions (but not paralysis)
    - Fast execution after clarity
    - Explicit and visual architecture
    - Progress with traceablity without reading novels
    - Resume anytime without rework
    - Hard stops on bad quality

Avoid:
    - over-engineered AI workflow system, that slows me down more than helps
    - specs generating instead of decisions
    - question answering theatre
    - agent talking more than coding
    - loosing speed on simple tasks

Minimal but sufficient memory:
    - README.md or PRODUCT.md - product durable context for fast onboarding and product vision
    - ARCHITECTURE.md - technical durable context to enforce consistency of tech decisions
    - IDEAS.md - anything that can be considered for future work, but not elaborated yet, helps to resume work after a break
    - specs/ folder that conatins elaborated specs on bigger features: new ones - provide quality context for implementation, implemented ones - provide historical context
    - DECISIONS.md - important architectural and product decisions with reasonable rationale

Definition of Done:
    - [ ] Feature or task implemented
    - [ ] Tests generated and pass
    - [ ] Code review: No duplication, no dead code, no security issues, consistent with ARHITECTURE.md and DECISIONS.md
    - [ ] Memory updated
    - [ ] Code committed

Close alternatives:
    - Superpowers plugin [https://github.com/obra/superpowers]
    - Garry Tan's GStack [https://github.com/garrytan/gstack]

## Proposed solution: Craft - lightweight SDD: from guided discovery to delegated delivery.  - May, 2026

Craft is an SDD plugin for people who stay top-level decision makers — product owners, directors, CTOs — and want agents to reduce coding effort, not control.

**Maximum leverage, not maximum automation.** Human judgment on decisions; agent execution after.

The split:

- agent: explore, analyze, propose, implement, test, review, update memory, [deploy, run, monitor]
- human: intent, motivation, clarify, steer, choose tradeoffs, approve decisions

### Problem

Fast generation hides early mistakes. The first pass looks good while the data model is wrong, boundaries are accidental, ownership is unclear, and tests are shallow — maintenance cost already baked in. The model doesn't see the debt; the user sees it only after more features make rewrite cheaper than repair.

Craft targets this failure: **make bad foundations visible before they become code.** More specs are not the goal — earlier decision visibility is.

### Differentiator

The wedge: **token-frugal, decision-first discovery.** No detailed planning unless it changes the outcome. Ask only what changes the solution.

The agent explores. It finds the hidden decisions. It surfaces them while they are still cheap to change, and lets the user steer. This is a conversation, not a questionnaire:

- "I found this constraint. It implies two designs."
- "I recommend this one because ownership stays clear."
- "The faster option makes this future feature harder. Which one fits your intent?"

### Visible decisions

Some decisions are expensive to undo. They must surface early — in the conversation, then as a diff the user approves. A decision first seen in the finished spec was found too late.

How it works: the agent names each decision as it finds it, states the tradeoff, recommends one, and waits. Diagrams carry the structure that words can't — system boundaries, data model, flow, state, ownership. They are review tools, not decoration. They let the user catch a wrong foundation before code piles on top of it.

The decisions that matter: data model & ownership · component boundaries · source of truth · API contracts · persistence & migration · state & lifecycle · dependencies · architecture-shaping UX flows · test strategy · scope cuts. Staying silent on any of these is a failure.

### The three skills

`prod` → `PRODUCT.md` — what constrains future decisions: who has the problem, which problem matters, solution direction, value to preserve, in/out of scope, hard constraints, success signals. Not a roadmap or pitch. Stops agents treating every task as local code work.

`arch` → `ARCHITECTURE.md` — the engineering map as a review surface, not an encyclopedia: components & responsibilities, ownership boundaries, core entities & data ownership, communication, entrypoints & commands, non-obvious conventions, key risks & decisions. Template is a checklist; emit only what matters for this system.

`spec` → a build-ready decision record. It does two jobs: fast human review, and execution by an agent with no prior context. Too short hides decisions. Too long buries them. So: review brief first. Execution detail only where it removes ambiguity for the executor. Acceptance criteria as stop conditions. Explicit non-goals. Rejected alternatives when they explain the choice. Data, API, and architecture impact when it matters. Compressed thinking — not a transcript, not an essay.

Then `/goal`, or any headless executor, builds from the spec with no extra context and no silent redesign.

### Memory

Prevents archaeology. Must answer: where are we? why this choice? what's next?

- `PRODUCT.md` — product intent and constraints
- `ARCHITECTURE.md` — system shape, boundaries, stack, commands, conventions
- `DECISIONS.md` — product and architecture decisions with rationale
- `IDEAS.md` — parked scope needing elaboration

If memory becomes a prose dump, it failed.

### Quality gate

Delegated coding needs hard stops. Done means: behavior implemented · tests written and passing · acceptance criteria met · no duplication · no dead code · no obvious security issue · no contradiction with decisions · memory updated · changes committed. Not "looks done." Verified done.

### Avoid

Architecture hidden in code · lengthy questionnaires · accidental data models · documentation archaeology · heavy process for tiny tasks · bikeshedding.
