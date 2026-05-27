<!--
Skeleton for docs/specs/YYYY-MM-DD-nnn-<slug>.md, the implementation handoff.
-->

# <Feature> — Spec

**Date:** YYYY-MM-DD
**Status:** Draft | Ready to build
**Target:** <module/area this touches>

## Goal

What this delivers, the motivation and value.
State key assumptions.

## Acceptance criteria

The verifiable conditions that define done.

- [ ] <observable condition, e.g. "POST /x with body Y returns 201 and persists Z">
- [ ] <test/command that must pass, e.g. "`./gradlew :svc:test` green">

## Decisions

The choices that shape the implementation, one line each. Link rationale to `ADR.md`/`DECISIONS.md`.

## Scope

- **In:** what this feature includes.
- **Out / later:** what it explicitly does not (deferred items go to `IDEAS.md`).

## Context (as found in the code)

Real file paths, the patterns/utilities to reuse, the data model and external calls involved.

## Approach

How it fits within `ARCHITECTURE.md`. ASCII sketch when interaction is non-trivial. The
files/modules to create or change and their responsibilities — one line each.

## Testing approach

What to test and at which layer, and how (frameworks, fakes, fixtures).

## Open items

Anything unresolved that could block the build. If empty: "None — ready to build."
