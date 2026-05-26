---
description: Define technical architecture, development standards based on product requirements
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

Apply the `sa` skill to accomplish this task.

## Prerequisites

Verify `docs/product.md` exists. If missing, instruct user to run `/1-define-product` first.

## Inputs

Read:

- `docs/product.md` - Product requirements and constraints
- Documents from Bibliography section for additional context
- `docs/architecture.md` (if exists) - Existing decisions to update

## Process

1. If `architecture.md` exists: identify what needs updating vs. preserving
2. Apply the `sa` skill methodology
3. Iterate: propose components → validate tech choices → refine (min 2 passes before output)
4. Ask user When uncertain, document open questions
5. Write/update `docs/architecture.md` using template below

## Architecture Template

Omit any section not relevant to this system. No placeholder text.

---

```markdown

# Architecture Definition

## Executive Summary

[Write 2-3 sentences describing the overall technical approach and key architectural decisions]

## High Level Components (Modules)


*Modules* are bigger parts of the system that developed in their own repositories or source folders. Usually each module corresponds 1+ deployable artifact. Ex.: backend, auth-service, admin-webapp.


| Module         | Location        | Primary Tech | Has UI | Responsibilitites |
|----------------|-----------------|--------------|--------|---|
| <module_name>  | `/<module_path>`| <tech_brief> | Yes/No | One line description |


## System Architecture

[Visualize architecture with the help of diagrams (select 3-4 more relevant):
 (1) High Level System Design - core system modules interaction.
 (2) Data Flow, Sequence or Activity Diagram; BPMN - for complex flow.
 (3) Core entities / ERD from business perspective.
 (4) State diagram if state machine is central]

## Technology Stack Decisions

[Justify major technical decisions per module with clear rationale]

### Module: <module_name>

[Describe tech stack, choice rationale and alternatives considered, including when applicable:
- API contracts
- programming language
- framework
- data storage: entities and DB
- queue/messaging
- caching
- observability
]

## Repositories layout

[Tree-like structure with comments]

## Development Rules and Conventions

[Patterns, best practices, codestyle, git workflow, etc.]

## Testing Strategy

[Test pyramid description:
- Unit/Integration/E2E
- Mocking
- Tools
]

## Security Requirements

### Authentication & Authorization

[User Authentication, Session timeout, RBA, rate limiting, API keys, OAuth]

### Data Protection

[Encryption, input validation, sanitizing, attack prevention (SQL injection/XSS/CSRF/etc)]

## Optimization Strategies

[Caching, indexing, batching, lazy loading, CDN]

## Deployment & Operations

[Environments, DevOps, IaaS, backups, rollback, failover, deployment: blue-green/rolling/canary, health checking, APM]

## Open Technical Questions

- [ ] [Pending decision that affects implementation]

```
