---
description: Sync feature definition with new files in feature folder or changes in product.md
argument-hint: [Feature ID]
---
# Command Instructions

Update the feature definition for "$1" by syncing with:
- New files added to the feature directory (mockups, documents, user stories, images)
- Changes in `product/product.md` that affect this feature
- User-specified updates based on conversation context

## Prerequisites Validation

First, verify that the feature exists before attempting to update:

```bash
# Check feature definition exists
if [ ! -f "product/features/$1/feature.md" ]; then
    echo "❌ Feature definition missing: product/features/$1/feature.md"
    echo "Run /add-feature $1 first to create the feature"
    exit 1
fi

echo "✅ Feature found: product/features/$1/feature.md"
echo "🔄 Analyzing changes to sync..."
```

## Context

You are a Senior Business Analyst updating a feature definition to reflect new information, files, or product changes.

**Required Reading:**

- `product/features/$1/feature.md` - Current feature definition
- `product/product.md` (if exists) - Product context and any recent changes
- All files in `product/features/$1/` - New mockups, docs, images, user stories
- Use the `ba` skill which provides the feature template structure

## Task

1. **Detect Changes**: Identify what has changed since feature.md was last updated
   - Check modification dates: feature.md vs other files in the directory
   - Compare product.md updated date vs feature.md updated date
   - Review conversation context for user-specified changes

2. **Analyze New Content**:
   - List all files in `product/features/$1/` directory
   - Identify new mockups (*.html, *.png, *.jpg, *.pdf)
   - Find new documentation (*.md files other than feature.md)
   - Look for user stories, requirements docs, or design references

3. **Sync Product Changes** (if product.md exists and was updated):
   - Check if feature priority changed in product.md
   - Look for updated business context or strategic changes
   - Identify new dependencies or constraints affecting this feature

4. **Apply User Context**:
   - Review conversation history for specific update requests
   - If unclear what to update, ask user for clarification
   - Focus updates based on user's explicit instructions

5. **Update Feature Definition**:
   - Integrate references to new mockups and documents
   - Update relevant sections based on product.md changes
   - Apply user-requested modifications
   - Update metadata: Updated Date, Status (if appropriate)
   - Preserve existing content unless explicitly updating
   - Maintain template structure and format

6. **Validate Updates**:
   - Ensure feature.md still follows template structure
   - Verify acceptance criteria remain clear and testable
   - Check that all sections are coherent and complete

## Update Guidelines

### When Syncing New Files
- **Mockups**: Add references in "User Interface Requirements" section
- **User Stories**: Enhance "User Story" and "Business Context" sections
- **Documents**: Incorporate into relevant sections (requirements, technical, etc.)
- **Images**: Reference in appropriate context (UI, design, architecture)

### When Syncing Product Changes
- **Priority Changes**: Update metadata and business context
- **Strategic Shifts**: Reflect in "Business Context" and "Business Value"
- **New Constraints**: Add to "Dependencies" or "Technical Requirements"
- **Scope Changes**: Update "Out of Scope" section

### When Applying User Requests
- **Be Specific**: Make precise changes based on user's instructions
- **Preserve Intent**: Don't remove important existing content
- **Ask if Unclear**: If user request is ambiguous, ask for clarification
- **Track Changes**: Note what was updated in the response

## Interaction Pattern

If the scope of changes is unclear or multiple options exist:

```text
Update clarification needed: [What aspect is unclear]

Based on the files/changes found, I can update:
1. [Most relevant update option] (recommended)
2. [Alternative update option]
3. [Another update option]
A. All of the above
S. Something specific (please describe)
E. Explain what changed and let me decide

Current changes detected:
- {list of new files found}
- {product.md changes if any}
- {user context if provided}
```

## Output Requirements

- Update `product/features/$1/feature.md` with synced content
- Update "Updated Date" in metadata to current date
- Consider updating "Status" if feature progressed (e.g., Discovery → Defined)
- Preserve template structure and formatting
- Provide clear summary of what was updated and why

## Summary Format

After updating, provide a concise summary:

```text
✅ Updated feature definition for {FXXX-FeatureName}

Changes applied:
- {specific change 1}
- {specific change 2}
- {specific change 3}

Files synced:
- {new file 1}
- {new file 2}

Metadata updated:
- Updated Date: {new date}
- Status: {new status if changed}
```
