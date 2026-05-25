# Conventions seed: Kotlin

<!-- Seed for forge arch. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent Kotlin engineer. -->

## Data & types

- Prefer immutable `val` and `data class`; model absence with nullables, not sentinels.
- Use sealed classes/interfaces for closed sets of states; exhaustive `when` (no `else` catch-all).

## Structure

- Functional decomposition first; package by feature, not by layer. Don't pre-create
  `service`/`repository`/`mapper` layers "in case".
- Keep functions small and pure where practical; push side effects to the edges.

## Errors & nullability

- Fail fast with clear exceptions or a `Result`/sealed error type — pick one per module, don't mix.
- No `!!` outside tests. Handle null at the boundary.

## Concurrency

- Structured concurrency with coroutines; scope tied to lifecycle. No `GlobalScope`.
- Suspend functions for I/O; never block a coroutine dispatcher thread.

## Tests

- See [rules-tests.md](rules-tests.md). Kotlin specifics: prefer JUnit5 + a single assertion
  style per module; fake at the boundary, don't mock `data class`es.
