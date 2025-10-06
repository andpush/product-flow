---
description: Generate 3 versions of UI design mockups for the product
argument-hint: [add_context]
allowed-tools: Task, Bash
---
# Command instructions

## Validation Gate

```bash
# Check product definition exists
if [ ! -f "product/product.md" ]; then
    echo "❌ Product definition missing: product/product.md"
    echo "Run /define-product [name] first"
    exit 1
fi

# Check initial documents exist
if [ ! -d "product/initial-docs" ]; then
    echo "❌ Initial documents missing: product/initial-docs/"
    echo "Create product/initial-docs/ with vision, requirements, and reference materials"
    exit 1
fi

# Check for content in initial folder
if [ -z "$(ls -A product/initial-docs/)" ]; then
    echo "⚠️ product/initial-docs/ folder is empty"
    echo "Add vision documents, requirements, screenshots, and reference materials"
    read -p "Continue with empty initial folder? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        exit 1
    fi
fi

echo "✅ Prerequisites validated - ready for mockup generation"
```

## Task Instructions

Generate three distinct UI design mockups, based on the product requirements, each with different layout approaches and visual styles:

**Variant 1 - Modern Minimalist**: Minimalist with generous white space, soft shadows, subtle gradients, modern typography (Inter, Open Sans), with professioal, calm and focused vibe.

**Variant 2 - Elegant & High-End**: Luxurious, sophisticated, refined vibe. Serif fonts like Playfair Display.

**Variant 3 - Professional Corporate**: Sharp edges, strong hierarchy, premium feel, Dark theme or sophisticated neutral palette. Enterprise-grade, trustworthy, polished vibe.

## Execution

Launch THREE ui-mockup-designer agents in parallel. For each variant, provide specific instructions about:

- additional context specified as the argument to this command call: $ARGUMENTS
- The variant name and number
- The visual style direction
- The output filename

After all three agents complete, provide the user with:

1. A short summary
2. The file paths to all three HTML files
3. A suggestion to open them in a browser to preview

Remember to run all three agents in a SINGLE message with multiple Task tool calls to execute them in parallel.
