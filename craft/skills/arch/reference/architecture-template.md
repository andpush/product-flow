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

Visualize the structure, interactions and the trust/ownership boundaries.
Prefer ASCII diagrams with <120 characters in width, mermaid for larger diagrams.
Include general system view, add more if it affect decisions:
- Data flow / sequence / activity view — for complex flow.
- Entity / ERD view — for modules with persistent data.
- State view — when state machine is central.

## Data model

The key entities and their relationships at a high level — not a full schema.
Use diagram or table view per schema.

## Directory layout

Where things live: top-levels tree of dirs/modules and what each holds. Enough to navigate without guessing.

## Dev / test / deploy

The commands and entrypoints to build, run, test, and deploy.

## Architecture drivers / risks

Only constraints and risks that shape architecture: performance, security, compliance, deployment,
scalability, observability, caching, reliability.

## Rules and Conventions

The coding conventions that aren't obvious or that this project deviates on — per stack if several, a subsection each.
