---
name: forge
description: Use for software development of a product feature, service, API, data model, schema. Covers intent capture, requirements brainstorming, architecture and tech-stack decisions, feasibility analysis, implementation via TDD, code review, verification, and project setup (greenfield scaffolding or brownfield derivation of conventions and architecture) and progress tracking. Invoke as `forge <command> [target]` (ground, frame, build, review, resume).
---

Frames intent into a buildable spec, builds it test-first, and keeps a light decision/idea trail. The human stays the decision-maker; the agent does the coding.

`forge` is the engineering counterpart to `impeccable`, it consumes `PRODUCT.md`, created manually or produced by `impeccable`. For visual/UI/UX work — use `impeccable` instead, not forge.

## Setup (non-optional)

Before any code edits, pass these gates. Skipping them produces generic work that ignores the project.

| Gate | Required for | What to do |
|---|---|---|
| `PRODUCT.md` exists and is substantive (not empty/placeholder, >200 chars). | all | Run `$impeccable teach` or ask the user to write `PRODUCT.md`. Never synthesize it from the prompt alone. |
| `ARCHITECTURE.md` exists and substantive. | all | Run `forge ground` first. |
| A confirmed spec exists in `docs/specs/` with no blocking open questions. | build | Run `forge frame <target>` first. |


Headless or subagent runs should state gate status before editing files:

```text
FORGE_PREFLIGHT: product=pass ground=pass spec=pass|n/a
```

`spec=pass` is only valid after a `frame` spec exists and the user resolved its open questions — not after merely summarizing intent.

### Context gathering

Read each role's file (use the repo's filename if it differs from the default in parentheses):

- **Product** (`PRODUCT.md`) — required. Users, purpose, tone, anti-references (impeccable's output).
- **Architecture** (`ARCHITECTURE.md`) — required, canonical contract. Components, stacks, boundaries,
  layout, entrypoints.
- **Conventions** (`rules.md`, + `rules-<stack>.md`) — required. Coding/tech-stack conventions.
- **Decisions** (`ADR.md` or `DECISIONS.md`) — durable decision log (auto-detect; prefer the existing one).
- **Ideas** (`IDEAS.md`) — parked future work.
- Latest **docs/specs/** entry for the target, if any.

If already loaded this session, don't re-read unless a command rewrote a file.

## Shared engineering laws

Apply to every command. Keep them; they are the whole point.

- **KISS / YAGNI.** Functional decomposition first. Don't pre-create layers or abstractions "in case".
- **Simpler approach wins.** If one exists, recommend it; push back on ceremony without justification.
- **No separate DTOs** unless the wire shape genuinely differs from the domain/store shape.
- **Reuse before adding.** Find the existing function/utility/pattern before writing new code.
- **Evidence before "done".** Never claim passing/fixed/complete without showing the command output that proves it.
- **Challenge, don't stall.** Surface weak decisions with a concrete better option; then move.
- Defer to the project's own `rules*.md` and `ARCHITECTURE.md` when more specific.

## Definition of Done

- [ ] Tests written (test-first where practical)
- [ ] Feature/task implemented
- [ ] Tests pass (output shown)
- [ ] Reviewed: no duplication, no dead code, no security issues, consistent with `DECISIONS.md`/`ADR.md`
- [ ] Memory updated (decisions/ideas)
- [ ] Committed

## Commands

| Command | Purpose | Reference |
|---|---|---|
| `ground` | Set up durable project context: rules, architecture, tech stack (greenfield-define or brownfield-derive). Run once. | [reference/ground.md](reference/ground.md) |
| `frame [target]` | Brainstorm intent + load coding context + decide → emit a self-contained spec. The backbone. | [reference/frame.md](reference/frame.md) |
| `build [target]` | Implement the spec test-first, via fresh subagents. | [reference/build.md](reference/build.md) |
| `review [target]` | Verification + code-quality gate. Hard stop on bad quality. | [reference/review.md](reference/review.md) |
| `resume` | Reconstruct where work stopped and propose the next move. | [reference/resume.md](reference/resume.md) |

Supporting references: [reference/decisions.md](reference/decisions.md) (how/when to record decisions and ideas), [reference/spec-template.md](reference/spec-template.md) (the spec skeleton `frame` produces), [reference/architecture-template.md](reference/architecture-template.md) (the `ARCHITECTURE.md` skeleton `ground` produces).

### Routing rules

1. **No argument** — show the command table as a menu and ask what they'd like to do.
2. **First word matches a command** — pass the setup gates, then load that command's reference and follow it. Everything after the command name is the target.
3. **First word doesn't match** — treat the whole argument as a `frame` target.

Setup gates and context load once; sub-commands don't re-invoke `forge`. If a gate sends you to `ground` or `frame` as a blocker, finish it, refresh context, then resume the original command.
