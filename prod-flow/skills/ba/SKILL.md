---
name: ba
description: Business Analysis, Requirements Analysis, Functionality Decomposition, Features Definition.
version: 1.0.0
---
# Business Analysis

Perform Business Analysis as a senior BA based on the business needs and requirements and come up with clear features decomposition.

## Core Principles

### Business Value First

- Focus on "what" and "why", not "how"
- Business-oriented features, not technical tasks

## Functionality Decomposition

### Epic

**Strategic initiative or large functionality unit**:

- Substantial business value with measurable KPIs
- Spans multiple sprints/releases
- Independent from other epics (parallel development)
- Groups related features
- Example: `Self-service portal`, `GDPR compliance`

### Feature

**Deliverable capability**:

- Belongs to one Epic
- Contains Functional Requirements
- May contain User Stories
- Has Acceptance Criteria
- Example: `Password reset`, `CSV export`

### User Story

**User-facing scenario**:

```
As a [role], I want to [capability], so that [value]
```

Use for: user interactions with clear personas

### Functional Requirements

**Explicit rules & specs** for technical/non-user-facing functionality:

- Business logic, validations, data models
- API contracts, security constraints
- Use structured format (YAML/JSON) for complex specs

### Acceptance Criteria

**Testable conditions** defining "done" for Features, Stories, and FRs:

- Format: `Given [context], When [action], Then [outcome]`
- Cover: happy path + edge cases + errors + performance
- Must be specific, measurable, verifiable

### Product Definition Checklist

- [ ] User personas / target audience defined
- [ ] Success metrics / business goals clear
- [ ] Error handling / edge cases specified
- [ ] Security / compliance requirements documented
- [ ] Performance expectations defined
- [ ] User roles / permissions clarified
- [ ] Integration requirements listed
- [ ] Data model / entities understood
- [ ] Clear scope (in/out)
- [ ] Explicit dependencies
- [ ] Testable AC (happy + edge + error cases)
- [ ] Structured format for complex specs
