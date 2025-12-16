---
name: slides
description: Create PPTX presentation slides deck from any text markdown file
version: 1.0.0
allowed-tools: Read, Write, Bash
---
# Create PPTX slides

1. Review the text, suggest corrections in case of real omissions.
2. Prepare slides markdown:
   - Split text into meaningful chunks using --- separator.
   - Use # Title or ## Title for slide headings. 
   - For nested topics: "Header: Subheader" format
   - Group by meaning, not size
   - Preserve original wording - it is well thought
   - Never remove any content! You can only hide lengthy explanations into the Speaker Notes defined as `<!-- Notes: ... -->` without cuts and abbreviations.
   - Some slides may contain multiline code that may not fit into one slide, it is ok, do not cut or split, user will handle it manually, so leave it as is.
3. Structure:
   - Add title slide (title, subheader, author and date)
   - Add agenda slide listing all significant topics
   - Section slides between major topics (heading only)
   - Content slides: heading + bullets/tables/paragraphs
4. Formatting supported:
   - Bullets: - item (nested with indentation)
   - Tables: standard markdown tables
   - Inline: **bold**, *italic*, `code`, [link text](url)
5. Generate PPTX: `python3 scripts/md2pptx.py slides.md -o "Title_ddHHMM.pptx"`
