# Recording decisions and ideas

Keep the durable trail terse — capture decisions, not novels.

## Where

- **Decisions** → `DECISIONS.md` or `ADR.md` — whichever the repo already has. If neither
  exists, create `DECISIONS.md`. Append-only.
- **Ideas** → `IDEAS.md` — anything worth considering later but not elaborated now.

Auto-detect the existing file before creating a new one; don't introduce a second log.

## When to record a decision

Record only what's significant and non-obvious: architecture/tech-stack choices, data-model
or schema commitments, an explicit trade-off where the rejected option was reasonable, or a
deviation from a default. Skip the obvious. If you'd want to know *why* in six months, record it.

## Decision entry format (terse)

```markdown
## YYYY-MM-DD · [component] · Short title

**Decision:** one sentence — what we chose.
**Why:** one or two sentences — why it beat the alternative.
```

Two to four lines. Follow the repo's established format if it differs.

## Idea entry format

```markdown
- [ ] YYYY-MM-DD · [area] — the idea in one line (why it might matter).
```

## When

The spec session records decisions as they're settled. Whoever executes the spec appends any
decisions that emerge during implementation.
