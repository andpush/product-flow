<!--
The skeleton `forge teach` produces at ARCHITECTURE.md (the canonical engineering contract).
Both branches — greenfield-define and brownfield-derive — write to this shape so it's consistent
across projects. Omit a section only if it genuinely doesn't apply. Keep it scannable; link out
to PRODUCT.md / rules*.md / ADR.md rather than restating them.
-->

# Architecture

**Status:** Draft | Current
**Updated:** YYYY-MM-DD

## Overview

One or two lines: what the system is and its shape (e.g. "modular monolith", "3 services + web").
Link `PRODUCT.md` for the why.

## Components

Each component/module: its responsibility (one line) and its stack. Table or list.

| Component | Responsibility | Stack |
|---|---|---|
| … | … | … |

## Boundaries & data flow

How components talk (calls, queues, shared DB) and the trust/ownership boundaries. ASCII diagram
when the interaction is non-trivial.

## Data model

The key entities and their relationships at a high level — not a full schema.

## Directory layout

Where things live: top-level dirs/modules and what each holds. Enough to navigate without guessing.

## Dev / test / deploy

The commands and entrypoints to build, run, test, and deploy. Point to `rules*.md` for conventions.

## Conventions

Pointer to the convention files that apply (`rules.md`, `rules-<stack>.md`), not their contents.
