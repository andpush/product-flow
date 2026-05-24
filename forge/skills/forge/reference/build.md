# forge build [target]

Implement the feature from its `frame` spec, test-first. The spec is the brief.

## Precondition

The Spec gate must pass: a confirmed `docs/specs/*-<target>.md` exists with no blocking
open questions. If it doesn't, run `forge frame <target>` first — do not improvise the
design here.

## How to execute

- **Work from the spec, not from memory.** Re-read the spec; it is the source of truth.
- **TDD.** For each unit of behavior: write a failing test → implement to pass → refactor.
  Cover acceptance criteria and the non-trivial logic; meet any targets in `rules*.md`.
  Don't chase a coverage number for its own sake.
- **Atomic commits.** One coherent step per commit, clear message. Branch first if the
  repo's workflow expects it (see `rules*.md`).
- **Reuse first.** Use the existing utilities/patterns the spec identified before adding new.
- **Stay consistent** with `ARCHITECTURE.md` and `DECISIONS.md`/`ADR.md`. If the spec turns
  out wrong mid-build, stop and flag it — don't silently diverge.

### Model + context strategy (subagent dispatch)

- Dispatch implementation to **fresh subagents** on a cheaper model (e.g. `model: sonnet`),
  each reading the spec cold as its full brief.
- Reserve the strong model for `frame` and `review`.
- Independent units in parallel; dependent ones in sequence.

Use the harness's **native task tracking** to sequence and track work. Do not invent a
`TASKS.md` mechanism.

## Done

When the spec's scope is implemented and tests pass (show the output), update memory per
[decisions.md](decisions.md) and commit. Then hand to `forge review <target>` for the
quality gate. Report completion in a few lines with evidence — no narrative.
