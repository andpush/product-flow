<!--
The skeleton `forge arch` produces at ARCHITECTURE.md (the canonical engineering contract).
Both branches — greenfield-define and brownfield-derive — write to this shape so it's consistent
across projects. Omit a section only if it genuinely doesn't apply. Keep it scannable; link out
to PRODUCT.md / ADR.md rather than restating them.
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
when the interaction is non-trivial. The dependency graph between components must be acyclic — call
out any cycle and how it's broken.

## Data model

The key entities and their relationships at a high level — not a full schema.

## Directory layout

Where things live: top-level dirs/modules and what each holds. Enough to navigate without guessing.

## Dev / test / deploy

The commands and entrypoints to build, run, test, and deploy.

## Rules and Conventions

The coding conventions that aren't obvious or that this project deviates on — per stack if several, a subsection each. End with the standing decision rule:

### Standing architectural decision rule

On any architectural choice: surface the trade-off, prefer the simpler option, challenge a weak default with a better concrete one — then move. No paralysis, no question-answering theatre. Ask the user one thing at a time; don't ask what you can verify.
