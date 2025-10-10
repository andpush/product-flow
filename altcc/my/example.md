Fetch(https://docs.claude.com/en/product/claude-code/slash-commands.md)
  ⎿  Received 15.3KB (200 OK)

⏺ Based on my analysis of the Claude Code documentation and your command definition, I've identified several issues
  with the syntax and structure:

  Issues Found:

  1. Missing Frontmatter: The command lacks YAML frontmatter which is recommended for Claude Code commands. It
  should include metadata like description and argument hints.
  2. Bash Code Blocks: The command contains bash code blocks that won't be executed by Claude. Claude Code expects
  the command content to be instructions for Claude, not bash scripts.
  3. Improper Structure: The command mixes bash execution blocks with Claude instructions, which doesn't align with
  Claude Code's expected format.
  4. Missing Argument Usage: The command doesn't properly use the $ARGUMENTS or $1 placeholders to reference the
  provided argument.

  Corrected Version in @define-product.md

---
    description: Create a comprehensive product definition from initial documents and stakeholder input
    argument-hint: [product_name]
    allowed-tools: Read, Write, Bash, Glob
---

    # Define Product

    Create a comprehensive product definition for "$1" from initial documents and stakeholder input.

    First, check if the `product/initial-docs/` directory exists and contains initial documents. If not, inform the user to
    create it and add their initial documents (requirements, research, etc.).

    If the directory exists and contains files, proceed with the analysis.

    ## Context
    You are a Product Manager analyzing initial documents to create a comprehensive product definition.

    Read all files in `product/initial-docs/` which may include:
    - Problem domain descriptions
    - Market research documents
    - Solution ideation notes
    - Meeting notes with stakeholders
    - Business requirements
    - Use cases and user journeys
    - MVP vision documents

    ## Task
    1. **Extract and Synthesize**: Identify key information about the product from all initial documents
    2. **Identify Gaps**: Find missing or contradictory information that needs clarification
    3. **Ask Questions**: Use numbered options to clarify uncertainties (provide 3-5 specific options when possible)
    4. **Generate Document**: Create a complete `product/product.md` using the template

    ## Analysis Guidelines
    - Focus on MVP scope - what's absolutely necessary for first release
    - Each feature should be implementable in 1-2 weeks maximum
    - Prioritize features using MoSCoW method (Must/Should/Could/Won't)
    - Consider technical feasibility and resource constraints
    - Include measurable success metrics

    ## Interaction Pattern
    When you need clarification, present options using this format:
    ```
    Question: [Specific question about unclear requirement]

    1. [Most likely option with brief rationale] (recommended)
    2. [Alternative option with trade-offs]
    3. [Another viable alternative]
    A. Another option (please specify)
    E. Explain more context about this decision
    P. Postpone this decision (add to open questions)
    ```

    Group related questions to minimize interruptions and maintain flow.

    ## Output Requirements
    - Create `product/product.md` using the product template
    - Be concise but complete in descriptions
    - List all open questions that could block implementation
    - Include specific, measurable success metrics
    - Ensure all features are right-sized for agile development

    ## Post-execution
    ```bash
    # Validate output was created
    if [ -f "product/product.md" ]; then
        echo "✅ Product definition created successfully"
        echo "📝 Review product/product.md and resolve any open questions before proceeding"
    else
        echo "❌ Product definition was not created"
        exit 1
    fi
    ```
