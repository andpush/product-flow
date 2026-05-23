---
description: Create detailed feature definitions based on all MVP features from product.md and using documentation analysis.
---
# Command Instructions

## Validation Gate

Verify `docs/product.md` exists; if not, stop and tell the user to run `/1-define-product` first.

## Your Mission

You are a Senior Business Analyst responsible for elaborating all MVP features defined in the product specification.

For each feature in the MVP scope from `docs/product.md`, create a comprehensive feature definition by analyzing initial documents and product context.

## Read

1. **Product Context**:
   - Read `docs/product.md` to understand the product and extract all MVP features

2. **Initial Documentation**:
   - Explore all files in `docs/initial/` folder and its subfolders.
   - Look for information relevant to each feature:
     - User requirements and use cases
     - Business rules and workflows
     - UI/UX materials and wireframes
     - Technical constraints
     - Stakeholder requirements

3. **Existing Features**:
   - Check `docs/features/` directory for any existing feature definitions
   - Review existing features to avoid duplication and ensure consistency

## Execution Strategy

For each identified feature in MVP scope perform the following steps:

1. **Extract Feature Information** from product.md:
   - Feature name (e.g., 'user-signup')
   - Feature description
   - Epic it belongs to
   - Priority level
   - Effort estimate
   - Main user story

2. Invoke `/5-add-feature [feature-name]` to create a comprehensive feature definition following the feature template.

## Output Requirements

After processing all MVP features:

1. **Feature Files**: Each feature should have `docs/features/[feature-id]/feature.md`
2. **Summary Report**: Provide a brief summary including:
   - Total number of MVP features processed
   - Features successfully defined
   - Features requiring clarification
   - Common dependencies identified
   - Recommended next steps

## Next Steps

After all MVP features are defined, suggest:

1. Create UI mockups for features requiring interface design: `/6-mockup-feature [feature_name]`
2. Create implementation plans: `/7-plan-feature [feature_name]`
3. Review architecture to support all features: `/3-define-architecture`

## Error Handling

If a feature cannot be defined due to missing information:

- Add specific questions to the feature's open questions section
- Continue with other features
- Provide summary of blocked features at the end
