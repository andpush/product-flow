---
description: Create detailed feature definitions based on all MVP features from product.md and using documentation analysis.
---
# Command Instructions

## Validation Gate

![ -f "product/product.md" ] || { echo "❌ Missing product/product.md. Run /define-product first."; exit 1; }

## Your Mission

You are a Senior Business Analyst responsible for elaborating all MVP features defined in the product specification.

For each feature in the MVP scope from `product/product.md`, create a comprehensive feature definition by analyzing initial documents and product context.

## Read

1. **Product Context**:
   - Read `product/product.md` to understand the product and extract all MVP features

2. **Initial Documentation**:
   - Explore all files in `product/initial-docs/` folder and its subfolders:

   !ls -AR product/initial-docs/

   - Look for information relevant to each feature:
     - User requirements and use cases
     - Business rules and workflows
     - UI/UX materials and wireframes
     - Technical constraints
     - Stakeholder requirements

3. **Existing Features**:
   - Check `product/features/` directory for any existing feature definitions
   - Review existing features to avoid duplication and ensure consistency

## Task

For each feature identified in the MVP scope:

1. **Extract Feature Information** from product.md:
   - Feature ID (e.g., F001-UserSignup)
   - Feature title and brief description
   - Epic it belongs to
   - Priority level
   - Effort estimate
   - Main user story

2. **Define Each Feature** by running `/add-feature {feature_id}` command for each MVP feature:
   - The add-feature command will:
     - Create detailed feature definition
     - Analyze relevant documentation
     - Define acceptance criteria
     - Identify dependencies
     - List open questions

3. **Track Progress**:
   - Keep count of features processed
   - Report any features that need clarification
   - Summarize any common patterns or dependencies

## Execution Strategy

### Approach 1: Automated Feature Definition (Recommended)

For each MVP feature from product.md, automatically run:

```bash
/add-feature {feature_id}
```

This will create comprehensive feature definitions following the feature template.

### Approach 2: Batch Analysis (If needed)

If the product.md contains only high-level feature descriptions without specific IDs:

1. Extract all MVP features from product.md
2. Generate proper feature IDs (F001, F002, etc.)
3. For each feature, analyze initial docs for relevant information
4. Create feature definitions using the `product-discovery` skill which provides the feature template structure
5. Ask user for clarifications when needed

## Output Requirements

After processing all MVP features:

1. **Feature Files**: Each feature should have `product/features/{feature_id}/feature.md`
2. **Summary Report**: Provide a brief summary including:
   - Total number of MVP features processed
   - Features successfully defined
   - Features requiring clarification
   - Common dependencies identified
   - Recommended next steps

## Feature Definition Quality Checklist

Each feature definition should meet these criteria:

- [ ] Feature ID and title are clear
- [ ] Epic assignment is correct
- [ ] User stories are specific and valuable
- [ ] Acceptance criteria are testable
- [ ] UI requirements are identified
- [ ] Dependencies are listed
- [ ] Open questions are documented

## Next Steps

After all MVP features are defined, suggest:

1. Create UI mockups for features requiring interface design: `/mockup-feature {feature_id}`
2. Create implementation plans: `/plan-feature {feature_id}`
3. Review architecture to support all features: `/define-architecture`

## Progress Tracking

As you process features, maintain a running list:

```
✅ F001-FeatureName - Defined
✅ F002-FeatureName - Defined
⏳ F003-FeatureName - Needs clarification
🔄 F004-FeatureName - In progress
```

## Error Handling

If a feature cannot be defined due to missing information:

- Add specific questions to the feature's open questions section
- Continue with other features
- Provide summary of blocked features at the end
