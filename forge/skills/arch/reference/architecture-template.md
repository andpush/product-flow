<!--
The skeleton `arch` produces at ARCHITECTURE.md (the canonical engineering contract).
Omit a section only if it genuinely doesn't apply. Keep it scannable; link out
to PRODUCT.md rather than restating them.
-->

# Architecture

**Status:** Draft | Current
**Updated:** YYYY-MM-DD

## Overview

One or two lines: what the system is and its shape.
Link `PRODUCT.md` for the why.

## Components

For each component/module: its responsibility (one line) and its stack.

| Component | Location | Responsibility | Tech Stack | Entry point |
|---|---|---|---|---|
| … | … | … | … | … |

## System Architecture

Visualize how components talk (calls, queues, shared DB) and the trust/ownership boundaries.
Prefer ASCII diagrams with <120 characters in width, mermaid for larger diagrams.
Select 2-3 relevant diagrams:
 (1) High Level System Design - core system modules boundaries and interaction (mandatory).
 (2) Data Flow, Sequence or Activity Diagram; BPMN - for complex flow.
 (3) Core persistent entities or ERD from business perspective - for modules with persistent data.
 (4) State diagram if state machine is central.

## Data model

The key entities and their relationships at a high level — not a full schema.
Use diagram or table view per schema.

## Directory layout

Where things live: top-levels tree of dirs/modules and what each holds. Enough to navigate without guessing.

## Dev / test / deploy

The commands and entrypoints to build, run, test, and deploy.

## Non-functional requirements

Only those, affecting the solution architecture

## Crosscutting aspects

Deployment strategy, Scalability, Observability, APM, caching.

## Rules and Conventions

The coding conventions that aren't obvious or that this project deviates on — per stack if several, a subsection each.
