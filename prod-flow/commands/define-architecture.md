---
description: Define technical architecture, development standards based on product requirements
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

Apply the `architecture` skill throughout this task.

## Prerequisites

Verify `product/product.md` exists. If missing, instruct user to run `/define-product` first.

## Inputs

Read:

- `product/product.md` - Product requirements and constraints
- Documents from Bibliography section for additional context
- `product/architecture.md` (if exists) - Existing decisions to update
- `./**/CLAUDE.md`, `./**/AGENTS.md` (if exists) - Development preferences

## Process

1. If `architecture.md` exists: identify what needs updating vs. preserving
2. Follow `architecture` skill
3. Iterate: propose components → validate tech choices → refine (min 2 passes before output)
4. Ask user When uncertain, document open questions
5. Write/update `product/architecture.md` using template below

## Architecture Template

Omit any section not relevant to this system. No placeholder text.

---

```markdown

# Architecture Definition

## Executive Summary

[Write 2-3 sentences describing the overall technical approach and key architectural decisions]

## Core Principles

## System Architecture

[Visualize architecture with the help of diagrams (select 3-4 more relevant):
 (1) High Level System Design - only core system modules in the context of interacting actors,
 (2) Data Flow,
 (3) Sequence or Activity Diagram or BPMN - if complex flow,
 (4) ERD (business perspective),
 (5) State diagram if state machine is central]


### Modules

Here, *modules* are bigger parts of the system that developed in their own repositories or source folders. Usually each module corresponds 1+ deployable artifact.

[
List main modules that are stored in separate root directories or repositories.
Modules can be a backend, a service name, web app, mobile app, etc.
]

| Module         | Location        | Primary Tech | Has UI |
|----------------|-----------------|--------------|--------|
| <module_name>  | `/<module_path>`| <tech_brief> | Yes/No |


## Technology Stack Decisions

[Justify major technical decisions per module with clear rationale]

### Module Tech Stack: <module_name>

#### Primary Framework

- **Choice**:
- **Rationale**:
- **Alternatives Considered**:

#### Supporting Technologies

[Important dependncies and libraries. For frontends it could be styling, state management, etc.]

#### Persistent Data [if applicable]

[Entities list]

## Development Guidelines

### Code Organization

[Tree-like structure with comments]

### Coding Conventions

**Code Style**:

- **Formatter**:
- **Linter**:

**Git Workflow**:

- **Branch Strategy**: [Git Flow/GitHub Flow/Feature branches]
- **Commit Messages**: [Conventional Commits/Custom format]
- **PR Requirements**: [Review approval/Tests passing/No conflicts]

## Testing Strategy

**Test Pyramid**:

- **Unit Tests**: [>70% coverage required]
  - Test individual functions and components
  - Mock external dependencies
  - Fast execution (<100ms per test)

- **Integration Tests**: [API endpoints/Database operations]
  - Test component interactions
  - Use test database/environment
  - Verify data flow and business logic

- **End-to-End Tests**: [Critical user workflows]
  - Test complete user journeys
  - Use staging environment
  - Cover happy path and key error scenarios

**Testing Tools**:

- **Unit**: [Jest/Pytest/Go test/JUnit]
- **Integration**: [Supertest/TestClient/REST Assured]
- **E2E**: [Cypress/Playwright/Selenium]

## API Contracts

**API**:
**Authentication**: [JWT/OAuth 2.0/API Keys/Session-based]
**Conventions**:

## Security Requirements

### Authentication & Authorization

- **User Authentication**: [Method and requirements]
- **Session Management**: [Approach and timeout]
- **Role-Based Access**: [Roles and permissions]
- **API Security**: [Rate limiting/API keys/OAuth]

### Data Protection

- **Data Encryption**: [HTTPS for all communications]
- **Input Validation**: [Validate and sanitize all user inputs]
- **SQL Injection Prevention**: [Use parameterized queries/ORM]
- **XSS Protection**: [Escape output, Content Security Policy headers]
- **CSRF Protection**: [Tokens/Same-site cookies/Other]

## Optimization Strategies

- **Caching**: [Strategy and duration]
- **Database**: [Proper indexing, query optimization]
- **Frontend**: [Code splitting, lazy loading, image optimization, CDN]

## Deployment & Operations

### Environment Strategy

- **Development**: Local development with [database and services]
- **Staging**: Production-like environment for final testing
- **Production**: [Hosting platform] with [backup and monitoring]

### Deployment Process

1. **Code Review**: All changes require peer review and approval
2. **Automated Testing**: All tests must pass in CI pipeline
3. **Staging Deployment**: Deploy to staging for final validation
4. **Production Deployment**: [Deployment strategy: blue-green/rolling/canary]
5. **Health Checks**: Verify deployment success and system health

## Monitoring & Maintenance

- **Application Monitoring**: [Error tracking/Performance monitoring]
- **Infrastructure Monitoring**: [Server health/Database performance]
- **Logging**: Centralized logging with [retention policy]
- **Backup Strategy**: [Frequency and retention]
- **Update Schedule**: [Security patches/Dependency updates]

## Open Technical Questions

- [ ] [Pending decision that affects implementation]

```
