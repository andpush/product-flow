---
name: slides
description: Create PPTX presentation slides deck from any text markdown file
---
# Create PPTX slides

1. Review the text, suggest corrections in case of real omissions.
2. Prepare slides:
   - Split text into meaningful slide chunks. Group by meaning, not size
   - Content and wording are well thought, do not change it without a need
   - Only cosmetic changes allowed for presentation style
   - Instead of removal hide lengthy explanations into the Speaker Notes defined as `<!-- Notes: ... -->`
3. Use succinct titles. For nested topics: "Header: Subheader" format
4. Add the title slide with the title, subheader, author and date
5. Add agenda slide listing all significant topics
6. Add slides delimiting sections between different topics
7. Generate PPTX using `md2pptx.py` script

Save as `<title>_<ddHHMM>.pptx`
