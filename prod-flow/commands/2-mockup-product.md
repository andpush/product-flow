---
description: Generate 3 versions of UI design mockups for the product
argument-hint: [add_context]
---
# Command instructions

## Validation Gate

Verify `docs/product.md` exists; if not, stop and tell the user to run `/1-define-product` first.

If `docs/initial/` is missing or empty, warn the user (vision docs, requirements, screenshots, and reference materials belong there) and ask whether to continue before generating mockups.

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
- The output path and filename

After all three agents complete, provide the user with:

1. A short summary
2. The file paths to all three HTML files
3. A suggestion to open them in a browser to preview

Remember to run all three agents in a SINGLE message with multiple Task tool calls to execute them in parallel.
