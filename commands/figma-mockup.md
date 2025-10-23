---
description: Based on Figma design, generate UI mockup (clickable prototype) as HTML file,  with extracted styles and assets.
argument-hint: <figma_url> [additional_instructions]
allowed-tools: Task, Bash
---
# Command instructions

Generate a UI mockup based on the provided Figma design, extracting visual styles, components, and assets to create a high-fidelity HTML prototype.

## Validation Gate

```bash
# Check product definition exists
if [ ! -f "product/product.md" ]; then
    echo "❌ Product definition missing: product/product.md"
    echo "Run /define-product [name] first"
    exit 1
fi

# Extract Figma URL from arguments
FIGMA_URL=$(echo "$ARGUMENTS" | grep -oE 'https://[^ ]+figma[^ ]*' | head -1)

if [ -z "$FIGMA_URL" ]; then
    echo "❌ Figma URL required"
    echo "Usage: /figma-mockup <figma_url> [additional_instructions]"
    echo "Example: /figma-mockup https://figma.com/design/abc123/MyDesign?node-id=1-2 use modern styling"
    exit 1
fi

echo "✅ Prerequisites validated"
echo "📐 Figma URL: $FIGMA_URL"
```

## Execution

1. Parse command arguments
2. Read product requirements: `product/product.md` and other files referenced there
3. Invoke tools in Figma MCP to get all the information about the design, neccessary to build pixel perfect copy in the form of html file with assets folder.
4. Build HTML Mockup:
   - Apply extracted design system (colors, fonts, spacing)
   - Implement layout matching Figma design
   - Add interactivity and responsive behavior
   - Use modern CSS and JavaScript
   - Can use Tailwind CSS (CDN) but customize with Figma design tokens
5. Save the output:
   - HTML file: `outputs/mockups/figma-mockup-[timestamp]-[###].html`
   - Assets folder: `outputs/mockups/figma-mockup-[timestamp]-[###]-assets/`
6. Provide the user with:
   - A brief summary of the mockup created
   - Instructions to open the HTML file in a browser
