# Conventions seed: Kotlin

<!-- Seed for forge teach. Adapt and fold into ARCHITECTURE.md's Conventions section.
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

- Test behavior, not implementation. Prefer real collaborators; fake only at the boundary
  (network, clock, filesystem). Coverage targets live in `ARCHITECTURE.md`, not hardcoded here.
