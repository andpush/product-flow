<!--
The skeleton `forge frame` produces at docs/specs/YYYY-MM-DD-nnn-<slug>.md.
This is the implementation handoff: written to be built from cold, by a different
session/model/subagent. Concise but self-sufficient. Omit any section that doesn't
apply — don't pad. Reference PRODUCT.md / rules*.md / ARCHITECTURE.md, don't restate them.
-->

# <Feature> — Spec

**Date:** YYYY-MM-DD
**Status:** Draft | Ready to build
**Target:** <module/area this touches>

## Goal

One or two sentences: what this delivers and the user value. State key assumptions.

## Context (as found in the code)

What exists today that this builds on — real file paths, the patterns/utilities to reuse,
the data model and external calls involved. Enough that a cold reader doesn't have to
re-explore.

## Decisions

The choices that shape the implementation, each one line. Link the rationale to
`DECISIONS.md`/`ADR.md` rather than re-arguing it here.

## Architecture / approach

How it fits the system. An ASCII sketch when a flow or component interaction is non-trivial.
New components/files and their responsibilities.

## Scope

- **In:** what this feature includes.
- **Out / later:** what it explicitly does not (deferred items go to `IDEAS.md`).

## Affected components

List the files/modules to create or change, with a one-line note each.

## Testing approach

What to test and at which layer (unit / integration / e2e), and how (frameworks, fakes,
fixtures). The strategy, not a step-by-step plan.

## Open items

Anything still unresolved that could block the build. If empty, say "None — ready to build."
