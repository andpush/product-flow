# rules-typescript (seed)

<!-- Seed for forge ground. Adapt and trim into the project's rules.md / rules-ts.md.
     Keep only what isn't obvious to a competent TS engineer. -->

## Types

- `strict` on. No `any`; use `unknown` + narrowing at boundaries. Prefer `type`/`interface` over
  loose objects.
- One shared type per concept across client/server/store. **No parallel `*Dto`** unless the wire
  shape genuinely differs — validate at the edge (e.g. zod) and reuse the inferred type inward.
- Discriminated unions for closed state sets; exhaustive `switch` with a `never` default guard.

## Structure

- Package by feature, not by layer. Don't pre-create `services/`/`models/`/`utils/` scaffolding
  before there's something to put in them.
- Small pure functions; isolate side effects (I/O, DOM, network).

## Async & errors

- `async/await`, not raw `.then` chains. Never leave a promise unawaited (`no-floating-promises`).
- Throw `Error` subclasses or return a typed result — one convention per module.

## Tooling

- One package manager, committed lockfile. Type-check and lint in CI; format on commit.
- Test behavior via the public surface; mock only true boundaries. Coverage targets live in
  `ARCHITECTURE.md`, not hardcoded here.
