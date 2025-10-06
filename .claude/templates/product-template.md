<!-- Use this template when creating `product/product.md` with /define-product command -->

# Product Definition

| **Product Name:**  | [PRODUCT_NAME] |
|--------------------|----------------|
| **Creation Date:** | [YYYY-MM-DD]   |
| **Status:**        | [Draft/Defined] |

## Product Purpose

[ The What: One clear paragraph explaining what this product does and its core value proposition ]

## Target Audience

[ The Who ]

- **Primary Users**: Specific user persona and their characteristics
- **User Needs**: What specific problems they need solved
- **Context**: When and where they would use this product*

## Problem Solved

[ The Why, including: ]

- **Problem Statement**: *The specific problem this product addresses*
- **Current Pain Points**: *What users struggle with today*
- **Impact**: *Why this problem matters (cost, time, frustration)

## Solution Description

[ The How, including: ]

- **Core Approach**: *How the product solves the problem*
- **Key Features**: *3-5 main capabilities that deliver value*
- **Differentiation**: *What makes this solution unique*

## Competitive Analysis and UVP

| Competitor | Their Approach | Our Advantage |
|------------|----------------|---------------|
| [Name] | [Brief description] | [Our differentiation] |

## Constraints & Assumptions

[List time, budget, team, and technical constraints and assumptions, if they are not mentioned elsewhere, do not duplicate requirements here]

## Success Metrics

[Specify measurable business-oriented indicators of product success, do not duplicate requirements here]

- User Adoption: [target_number] active users by [date]
- Engagement: [target_percentage] weekly retention rate
- Business: [revenue/cost_savings/other_metric]
- Quality: [performance/satisfaction_metric]

## UI/UX Guidelines

- **Platforms**: [Web/Mobile/Desktop]
- **Design System**: [Name or description]
- **Reference**: [Link to design examples or style guide]
- **Accessibility**: [WCAG 2.1 Level AA compliance required]
- **Responsive**: [Screen sizes and devices]

## Non-functional Requirements, SLA

[ Only specify if known and affects the architecture ]

- **Performance**: [P95 Response time < 200 ms, P95 Page Load < 2s]
- **Availability**: [99.9% uptime. Maintenance window: weekly, on Wednesday 23:00 - 0:00]
- **Security**: [Specific security requirements]
- **Scale**: [Number of concurrent users], [data volume]
- **Integration**: [External systems or APIs required]

## Bibliography

[List references to initial files used as sources to generate this content, identified as most relevant for product requirements]

## High Level Decomposition - Epics

- [Epic Name 1]
- [Epic Name 2]
- [Epic Name 3]

## Core Functionality (MVP)

### Epic: [Epic Name]

#### [F001-UserSignup]

**Brief description**: [Feature description]

**Main User Story**: As a [user_type], I want to [action] so that [benefit]

**Priority**: [Must Have/Should Have/Nice to Have]

**Effort Estimate**: [XS (<1 day)/S (1-2 days)/M (3-5 days)/L (1-2 weeks)/XL (>2 weeks)]

#### F002-UserLogin

[ See example above ]

### Epic: [Next Epic Name]

#### [F003-TopMenu]

[ See example above ]

## Future Features (Post-MVP)

(Features for future releases, not a focus for now, but may affect architecture or data model)

- [Possible future feature brief description]
- [Possible future feature brief description]
- [Possible future feature brief description]

## Open Questions

Critical decisions that need resolution before implementation.

### Question: [Question to clarify]

**Why it matters**: [Explanation]

**Possible Options**: [Numbered list of options]

**Answer**: **TBD**

<!-- AI instructions -->

## Template Usage Instructions

- **Follow the template**: Stick to the template formatting. Exception: motivated customisation is allowed, e.g. you can add or remove sections depending on the project needs.
- **Be Concise and Specific**: Be concise but complete in descriptions. Be specific: use concrete numbers and dates.
- **No fake data**: Do not guess or hallucinate numbers and values. All data should grounded on initial source files or explicelty provided bu user. Ask user when in doubt.
- **Replace Placeholders**: All items in [brackets] should be replaced with actual values. Remove all [guidance text] after filling in real content.
- **Document uncertainties**: List all open questions that could block implementation.

## Product Defined Status Checklist

The initial product status is Draft unless the product definition complete. The Defined status criteria:

- [ ] Product purpose is clear and compelling
- [ ] Target audience is specific and well-defined
- [ ] All MVP features have clear user stories
- [ ] No critical open questions remain - has answers other than TBD
- [ ] Technical constraints are realistic
