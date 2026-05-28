<!--
Seed menu for the `arch` skill's `Rules and Conventions` step — consulted, not emitted.
Pick the sections that fit the chosen stack, adapt with the user, keep only what isn't
obvious to a competent engineer, and fold the result into ARCHITECTURE.md. Do NOT copy
sections for stacks the project doesn't use.
-->

# Conventions seed

## General

- Avoid duplications, use DRY principle.
- Avoid artificial complexity, stick to KISS/YAGNI principles.
- Prefer immutable data structures.
- Ground the implementation on requirements. Strictly adhere to the provided context. Do not invent or hallucinate features, technologies, or dependencies that aren't specified.
- Separate concerns with a clear folder structure; package by feature where practical.

**Surgical Changes:**

- Touch only what you must. Match existing style.
- Minimum code/complexity that solves the problem.
- Don't refactor unrelated code.
- Remove imports/functions/variables that YOUR changes made unused.
- Every changed line should trace directly to the request.

## Testing

- **TDD** for APIs and before refactoring: RED → GREEN → REFACTOR.
- **Pyramid**: many unit (fast), some integration, few end-to-end (Playwright) — slow but load-bearing.
- Test behavior through the public surface, not implementation details; one clear intent per test, named for the behavior it pins.
- Fake only true boundaries (network, filesystem, clock, randomness, payments); never mock your own business logic.
- Cover the acceptance criteria and the non-trivial/error paths — not lines for their own sake.

## Backend

- Simplified layered architecture: API -> Service -> Store.
- Expose services via REST unless another protocol is explicitly specified.
- Prepare for containerization and cloud deployment.

## Web app

- One component library and one styling system per app — don't mix paradigms.
- Component-first: small, composable, single-purpose components over large ones.
- Keep state close to where it's used; lift it only when genuinely shared.
- Accessibility is a requirement, not a polish pass: semantic HTML, keyboard paths, WCAG AA.
- Fetch the framework's current docs when unsure rather than guessing an API.

## Mobile

- Follow the platform/language's official style guide (e.g. Effective Dart for Dart).
- Pick one state-management approach and apply it consistently; don't mix paradigms.
- Theme centrally (e.g. `MaterialApp.theme`); don't hardcode colors/sizes in widgets.
- Separate concerns with a clear folder structure; package by feature where practical.
- Small, composable widgets over large ones.
- Responsive by construction: prefer flex/relative sizing over hardcoded dimensions.
- Use the platform logger (e.g. `dart:developer` `log`), never `print`/`debugPrint`.

## Kotlin

- Prefer immutable `val` and `data class`; model absence with nullables, not sentinels.
- Use sealed classes/interfaces for closed sets of states; exhaustive `when` (no `else` catch-all).
- Functional decomposition first; package by feature, not by layer. Don't pre-create
  `service`/`repository`/`mapper` layers "in case".
- Keep functions small and pure where practical; push side effects to the edges.
- Fail fast with clear exceptions or a `Result`/sealed error type — pick one per module, don't mix.
- No `!!` outside tests. Handle null at the boundary.
- Structured concurrency with coroutines; scope tied to lifecycle. No `GlobalScope`.
- Suspend functions for I/O; never block a coroutine dispatcher thread.

## TypeScript

- `strict` on. No `any`; use `unknown` + narrowing at boundaries. Prefer `type`/`interface` over
  loose objects.
- One shared type per concept across client/server/store. **No parallel `*Dto`** unless the wire
  shape genuinely differs — validate at the edge (e.g. zod) and reuse the inferred type inward.
- Discriminated unions for closed state sets; exhaustive `switch` with a `never` default guard.
- Package by feature, not by layer. Don't pre-create `services/`/`models/`/`utils/` scaffolding
  before there's something to put in them.
- Small pure functions; isolate side effects (I/O, DOM, network).
- `async/await`, not raw `.then` chains. Never leave a promise unawaited (`no-floating-promises`).
- Throw `Error` subclasses or return a typed result — one convention per module.
- One package manager, committed lockfile. Type-check and lint in CI; format on commit.
