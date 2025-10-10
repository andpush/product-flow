---
description: Generate UI mockup as HTML file, based on Figma design with extracted styles and assets
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

## Context

**Parse command arguments:**

1. **Figma URL** (required): URL containing node-id parameter. The URL should be supplied by user from the running Figma Desktop.
2. **Additional instructions** (optional): Any remaining text after the URL: [additional_instructions].

Example: `/figma-mockup https://figma.com/design/abc/file?node-id=1-2 use vibrant colors and add animations`

Read product requirements: `product/product.md` and other files referenced there.

## Execution

1. **Use cached Figma assets as you need:**:

    ```bash
    !ls product/figma-assets/
    ```

    Load pdf with the screenshot to familize with the expected overall UI design.

    ```bash
    !ls product/figma-assets/*.pdf
    ```

2. **Extract Figma Information**:
   - Parse the Figma URL to get fileKey and nodeId
   - Use MCP Figma tools to get full context for the frame url:
      - `mcp__figma-desktop__get_metadata`
      - `mcp__figma-desktop__get_variable_defs` - to extract all design tokens (colors, typography, spacing)
      - `mcp__figma-desktop__create_design_system_rules` - get design system
   - Invoke mcp__figma-desktop__get_code **for each relevant sub-nodes** to extract code and assets.

3. **Build HTML Mockup**:
   - Create HTML file referencing local assets (use relative paths to assets folder)
   - Apply extracted design system (colors, fonts, spacing)
   - Implement layout matching Figma design
   - Add interactivity and responsive behavior
   - Use modern CSS and JavaScript
   - Can use Tailwind CSS (CDN) but customize with Figma design tokens

4. **Output**:
   - HTML file: `outputs/mockups/figma-mockup-[timestamp]-[###].html`
   - Assets folder: `outputs/mockups/figma-mockup-[timestamp]-[###]-assets/`

5. Provide the user with:

- A brief summary of the mockup created
- The file path to the HTML file
- List of key design elements extracted from Figma
- Instructions to open the HTML file in a browser
