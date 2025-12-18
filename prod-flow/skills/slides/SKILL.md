---
name: slides
description: Create PPTX presentation slides deck from any text
version: 1.0.0
allowed-tools: Read, Write, Bash
---
Convert the text into a presentation deck in PPTX format.

1. Review text first; flag any apparent omissions or inconsistencies.

2. Prepare slides.md.
Format:
   - YAML frontmatter: title, subtitle (optional), author, date
   - `---` to separate slides
   - `#` Section dividers (heading only)
   - `##` Slide titles
   - Slide content: 
      - paragraphs/bullets
      - markdown tables when >3 data rows
      - when appropriate use 2 or 3 borderless column layout, delimiting columns with `||`
      - Speaker Notes: `<!-- Notes: ... -->`
Instructions: 
   - Group slides by meaning, not size
   - Preserve original wording verbatim (well thought out)
   - Do NOT remove or abbreviate any content
   - Allowed edits to match concise presentation style:
      - Move explanatory passages (>2 sentences) to Speaker Notes.
      - Move duplications into the Speaker Notes. 
   - **Leave multiline code blocks intact**, even if they overflow!
   - Add Agenda slide right after the title slide listing all sections
3. Generate PPTX using the `md2pptx.py`: 
   - Supported formatting: 
      - Bullets: * (nested items with indentation)
      - Tables: standard markdown tables
      - Inline: **bold**, *italic*, `code`, [link text](url)
   - Run the script: `python3 scripts/md2pptx.py slides.md -o "<title>-<ddHHMM>.pptx"`
