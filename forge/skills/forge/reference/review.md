# forge review [target]

The hard-stop quality gate. Prefer a clean context (or subagent) from the strong model, not
the one that wrote the code.

## Verify first (evidence before claims)

- Run the tests and **show the output**. No "should pass" — prove it.
- Run the build/lint the project uses. Report real results, including failures.
- Never assert passing/fixed/complete without the command output that demonstrates it.

## Review dimensions

Trace the changed code (entry points → logic → data layer → external calls) and flag
concrete, file:line findings:

- **Correctness** — logic errors, unhandled edge cases, race conditions, data integrity.
- **Security** — injection, hardcoded secrets, missing authz/validation.
- **Duplication & dead code** — repeated logic, unused code or deps, leftover scaffolding.
- **Consistency** — matches `ARCHITECTURE.md`, `rules*.md`, and `DECISIONS.md`/`ADR.md`;
  reuses existing patterns rather than reinventing.
- **Tests** — cover acceptance criteria and edge/error cases; verify behavior, not just lines.

## Output (terse)

A one-paragraph verdict (✅ good / ⚠️ needs work / ❌ blocked), then a short table:

| P | Area | Location | Issue | Fix |
|---|------|----------|-------|-----|
| P0 | … | file:line | … | … |

P0 = must fix before ship, P1 = should fix, P2 = optional. No score-out-of-10, no
sign-off tables, no boilerplate sections. If nothing in a dimension, omit it.

## Done

If clean: confirm the Definition of Done is met, ensure memory is updated, and commit.
If not: list the P0/P1 fixes and stop — bad quality is a hard stop, not a note for later.
