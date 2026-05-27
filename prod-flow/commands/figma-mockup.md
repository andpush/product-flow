---
description: Based on Figma design, generate UI mockup (clickable prototype) as HTML file,  with extracted styles and assets.
argument-hint: <figma_url> [additional_instructions]
---
# Command instructions

Generate a UI mockup based on the provided Figma design, extracting visual styles, components, and assets to create a high-fidelity HTML prototype.

## Validation Gate

Verify `PRODUCT.md` exists; if not, stop and tell the user to run `/1-define-product` first.

A Figma URL is required. If `$ARGUMENTS` contains no `figma.com` URL, stop and show usage:
`/figma-mockup <figma_url> [additional_instructions]`

## Execution

1. Parse the Figma URL and any extra instructions from `$ARGUMENTS`
2. Read product requirements: `PRODUCT.md` and other files referenced there
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
