---
description: Create a comprehensive product definition from initial documents and stakeholder input
argument-hint: product name
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

## Your Mission

Generate or update product definition in `product/product.md` based on the provided initial documentation.

Use the `ba` skill and the template below to guide the analysis.

## Context

User provided short [PRODUCT_NAME] as an argument to this command: $ARGUMENTS .
If command arguments not provided, deduce it from the context.

Explore the following files:

```bash
product/
├── initial-docs/**    # Initial documents to research
├── product.md         # (if exists) previous definition to update
```

`!ls -AR "product/initial-docs"`

Look for the files containing the most relevant and up-to-date information about the product:

- Product vision
- Business domain
- Problem statement
- Market research
- Solution ideation notes
- Meeting notes with stakeholders
- Business needs and requirements
- Use cases and user journeys

Load the UI materials if present:

- Design system, UI/UX guides
- Wireframes, reference UI
- Screenshots of competitors, similar or related solutions

## Task

1. **Analyse all initial documents**: THINK about:
   - the problem the product solves
   - actors and their actions
   - enitites and data-flow
   - constraints
2. **High Level Decomposition**:
   - Identify bigger tracks of functionality - Epics
   - Limit to a small number of epics (2-7)
   - Confirm the list of Epics with the User
3. **Functional Decomposition**: THINK about features to deliver:
   - Focus on MVP scope.
   - Features should be business-oriented, right-sized (not too granular), with clear business goals.
   - Consider technical feasibility and resource constraints.
4. **Identify Gaps and Inconsistencies**:
   - Are there any gaps in requirements?
   - Check for inconsistencies and ambiguous language.
   - Think what clarifications are absolutely necessary in order to start solutioning.
5. **Ask User for clarifications**:
   - Only ask user when the information is absolutely necessary to proceed
   - Be concise and crystall clear
   - Ask questions one at a time
   - Wait user definite answer before asking another question
   - Provide 2-3 numbered options when possible
   - Include brief rationale for recommended option

   ```markdown
   ===
   **Question**: [Specific question about unclear requirement]

   **Why it matters**: [A very brief explanation of what it affects]

   **Options**:

   1. Most likely or recommended option with brief rationale
   2. Alternative, with trade-offs
   3. Another - Please Specify [let the user to write]
   P. Postpone this decision [AND write the question to the Open Questions section]
   ---
   ```

6. **Generate Output**: Create/update the output file according to the template below.

   - Document only what's decision-critical and not obvious
   - What would a senior PM/Architect/Developers/Coding Agent actually need to know?
   - Be concise, avoid duplication
   - Be specific: use concrete numbers and dates. Do not guess, ask user when in doubt
   - List all open questions that could block implementation.

7. **Product Defined Status Checklist**

   The initial product status is Draft unless the product definition complete. The Defined status criteria:

   - [ ] Product purpose is clear and compelling
   - [ ] Target audience is specific and well-defined
   - [ ] All MVP features have clear user stories
   - [ ] No critical open questions remain - has answers other than TBD
   - [ ] Technical constraints are realistic

8. **Suggest user next steps:**
   - Run `/define-architecture` to define technical approach

---

## Product Definition Template

```markdown
---
Product:  [PRODUCT_NAME]
Created:  [YYYY-MM-DD]
Updated:  [YYYY-MM-DD]
Status:   [Draft/Defined]
---

# Product Definition

## Product Vision

[One paragraph]

## Problem Solved

**Problem Statement**: [The specific problem this product addresses]

**Impact**: [Why this problem matters (cost, time, frustration)]

## Target Audience

- **Primary Users**: [Persona or segment]
- **Looking for**: [Needs driving use]
- **Pain points**: [Problems driving use]

## Solution Description

[How the product solves the problem. Capabilities. Differentiation.]

## Competitive Analysis and UVP

| Competitor | Their Approach      | Our Advantage         |
|------------|---------------------|-----------------------|
| [Name]     | [Brief description] | [Our differentiation] |

## Constraints & Assumptions

[Time, budget, team, and technical constraints and assumptions, signinficant for planning and implementation]

## Success Metrics

[Specify at least one measurable business-oriented indicators of product success]

- User Adoption [target_number] active users by [date]
- Engagement: [target_percentage] weekly retention rate
- Business: [revenue/cost_savings]
- Loyalty and Satisfaction: [DAU/MAU ratio, Avg Session Duration, etc.]

## UI/UX Guidelines

- **Platforms**: [Web/Mobile/Desktop]
- **Design System**: [Name or description]
- **Reference**: [Link to design examples or style guide]
- **Accessibility**: [WCAG 2.1 Level AA compliance required]
- **Responsive**: [Screen sizes and devices]

## Non-functional Requirements, SLA

[Specify only known requirements that affect the architecture]

- **Performance**: [P95 Response time < 200 ms, P95 Page Load < 2s]
- **Availability**: [99.9% uptime. Maintenance window: weekly, on Wednesday 23:00 - 0:00]
- **Security**: [Specific security requirements]
- **Scale**: [Number of concurrent users], [data volume]
- **Integration**: [External systems or APIs required]

## Bibliography

[List references to the most relevant initial files used as sources to generate this content]

## High Level Decomposition

### Epics

[List of Epics]

### Core Functionality (MVP)

---

| Feature | [001-TopMenu]  |
|-|-|
| Epic | [Landing Page] |
| Size | [XS/S/M/L/XL]  |
| Brief | [Feature description]  |
| Story | [Main User Story]     |

---

### Future Features (Post-MVP)

[May be postponed for future releases, but may affect architecture or data model]

## Open Questions

Critical decisions blocking implementation.

### Question: [Question to clarify]

**Why it matters**: [Explanation]

**Possible Options**: [Numbered list of options]

**Answer**: **TBD**
```
