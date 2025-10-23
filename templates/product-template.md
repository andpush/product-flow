<!-- Use this template when creating `product/product.md` with /define-product command -->

# Product Definition

| **Product Name:**  | [PRODUCT_NAME]  |
|--------------------|-----------------|
| **Creation Date:** | [YYYY-MM-DD]    |
| **Status:**        | [Draft/Defined] |

## Product Purpose

[One clear paragraph explaining what this product does and its core value proposition ]

## Target Audience

- **Primary Users**: [Specific user persona and their characteristics]
- **User Needs**: [What specific problems they need solved]
- **Context**: [When and where they would use this product]

## Problem Solved

- **Problem Statement**: [The specific problem this product addresses]
- **Current Pain Points**: [What users struggle with today]
- **Impact**: [Why this problem matters (cost, time, frustration)]

## Solution Description

- **Core Approach**: [How the product solves the problem]
- **Key Features**: [3-5 main capabilities that deliver value]
- **Differentiation**: [What makes this solution unique]

## Competitive Analysis and UVP

| Competitor | Their Approach      | Our Advantage         |
|------------|---------------------|-----------------------|
| [Name]     | [Brief description] | [Our differentiation] |

## Constraints & Assumptions

[List time, budget, team, and technical constraints and assumptions, if they are not mentioned elsewhere]

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

### Decomposition Hierarchy

```text
Epic (large groups of related functionality)
  └─ Feature (defines business capability as one or more User Stories and Functional Requirements)
      └─ User Story (specific user need/scenario)
          └─ SubTask (atomic unit of work within one component)
```

## Core Functionality (MVP)

### Epic: [Landing and Navigation]

#### Feature: [F001-Landing Page] ([Estimate XS/S/M/L/XL])

- **Brief description**: [Feature description]
- **Main User Story**: As a [user_type], I want to [action] so that [benefit]

#### Feature: F002-TopMenu

[...]

## Future Features (Post-MVP)

(Features for future releases, not a focus for now, but may affect architecture or data model)

- [Possible future feature brief description]

## Open Questions

Critical decisions that need resolution before implementation.

### Question: [Question to clarify]

**Why it matters**: [Explanation]

**Possible Options**: [Numbered list of options]

**Answer**: **TBD**

<!-- AI instructions -->

## Template Usage Instructions

- Be concise but complete in descriptions.
- Be specific: use concrete numbers and dates. Do not guess, if data not found in initial documents, ask user.
- List all open questions that could block implementation.

## Product Defined Status Checklist

The initial product status is Draft unless the product definition complete. The Defined status criteria:

- [ ] Product purpose is clear and compelling
- [ ] Target audience is specific and well-defined
- [ ] All MVP features have clear user stories
- [ ] No critical open questions remain - has answers other than TBD
- [ ] Technical constraints are realistic
