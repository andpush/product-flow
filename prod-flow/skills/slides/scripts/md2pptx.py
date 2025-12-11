#!/usr/bin/env python3
"""
Universal Markdown to PowerPoint Converter

Converts markdown files with --- slide separators into PPTX presentations.
Supports speaker notes, tables, bullets, and inline formatting.
"""

import re
import argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor


# ============================================================================
# CONFIGURATION
# ============================================================================

# Smoky dark blue color for titles and bullet markers
SMOKY_BLUE = RGBColor(0x36, 0x4F, 0x6B)  # #364F6B

# Default font
DEFAULT_FONT = "Heebo"


# ============================================================================
# PARSING FUNCTIONS
# ============================================================================

def split_slides(markdown_content):
    """Split markdown content on --- separators"""
    return re.split(r'\n---\n', markdown_content)


def extract_notes(slide_content):
    """
    Extract speaker notes from HTML comments: <!-- Notes: text -->
    Returns: (content_without_notes, notes_text)
    """
    pattern = r'<!--\s*Notes:\s*(.*?)\s*-->'
    notes_match = re.search(pattern, slide_content, re.DOTALL)
    content = re.sub(pattern, '', slide_content, flags=re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else ""
    return content.strip(), notes


def extract_title(content):
    """
    Extract first # or ## heading as title
    Returns: (title, remaining_content)
    """
    pattern = r'^#{1,2}\s+(.+?)$'
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Remove the title line from content
        content = re.sub(pattern, '', content, count=1, flags=re.MULTILINE)
        return title, content.strip()
    return "", content.strip()


def determine_layout(slide_index, title, content):
    """
    Determine slide layout based on content
    Returns: 0 (title), 1 (content), or 2 (section)
    """
    # First slide with minimal content = title slide
    if slide_index == 0:
        lines = [l for l in content.split('\n') if l.strip()]
        if len(lines) <= 3:
            return 0

    # Slide with only heading, no content = section divider
    if not content.strip():
        return 2

    # Everything else = content slide
    return 1


# ============================================================================
# CONTENT PROCESSING FUNCTIONS
# ============================================================================

def parse_bullets(content):
    """
    Parse markdown bullets into list with indentation levels
    Returns: list of (level, text) tuples
    """
    bullets = []
    for line in content.split('\n'):
        line_stripped = line.strip()
        if re.match(r'^[-*+]\s', line_stripped):
            # Calculate indentation level
            indent = len(line) - len(line.lstrip())
            level = 0 if indent < 2 else 1
            # Remove bullet marker
            text = re.sub(r'^[-*+]\s+', '', line_stripped)
            bullets.append((level, text))
    return bullets


def parse_table(content):
    """
    Parse markdown table into (headers, rows)
    Returns: (headers_list, rows_list) or None if not a valid table
    """
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    table_lines = [l for l in lines if l.startswith('|') and l.endswith('|')]

    if len(table_lines) < 2:
        return None

    # Parse header row
    headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]

    # Parse data rows (skip separator line at index 1)
    rows = []
    for line in table_lines[2:]:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        rows.append(cells)

    return headers, rows


def apply_formatting(paragraph, text, color=None):
    """
    Apply markdown inline formatting: **bold**, *italic*, `code`
    Creates separate runs for each format type
    """
    pattern = r'(\*\*(.+?)\*\*|\*(.+?)\*|`([^`]+)`|([^*`]+))'

    for match in re.finditer(pattern, text):
        run = paragraph.add_run()

        if match.group(2):  # **bold**
            run.text = match.group(2)
            run.font.bold = True
            run.font.name = DEFAULT_FONT
        elif match.group(3):  # *italic*
            run.text = match.group(3)
            run.font.italic = True
            run.font.name = DEFAULT_FONT
        elif match.group(4):  # `code`
            run.text = match.group(4)
            run.font.name = 'Courier New'
            run.font.size = Pt(14)
        elif match.group(5):  # plain text
            if not match.group(5):
                continue
            run.text = match.group(5)
            run.font.name = DEFAULT_FONT

        # Apply color if specified
        if color:
            run.font.color.rgb = color


# ============================================================================
# CONTENT ADDITION FUNCTIONS
# ============================================================================

def set_margins(text_frame):
    """Set reduced margins for text frames (half of default)"""
    text_frame.margin_left = Inches(0.05)   # Default ~0.1", now 0.05"
    text_frame.margin_right = Inches(0.05)
    text_frame.margin_top = Inches(0.025)   # Default ~0.05", now 0.025"
    text_frame.margin_bottom = Inches(0.025)


def add_bullets(text_frame, content):
    """Add bullet list to text frame with manual bullet characters"""
    bullets = parse_bullets(content)
    if not bullets:
        return

    text_frame.word_wrap = True
    set_margins(text_frame)

    BULLET_CHARS = ["•", "◦"]
    BLACK = RGBColor(0, 0, 0)

    for idx, (level, text) in enumerate(bullets):
        # Use first paragraph for first bullet, create new for rest
        p = text_frame.paragraphs[0] if idx == 0 else text_frame.add_paragraph()

        # Add indent if nested
        if level > 0:
            run = p.add_run()
            run.text = "    " * level
            run.font.name = DEFAULT_FONT
            run.font.color.rgb = BLACK

        # Add bullet character (blue)
        run = p.add_run()
        run.text = BULLET_CHARS[min(level, 1)] + " "
        run.font.name = DEFAULT_FONT
        run.font.color.rgb = SMOKY_BLUE

        # Add text content (black)
        apply_formatting(p, text, BLACK)


def add_table(slide, content):
    """Add table to slide"""
    table_data = parse_table(content)

    if not table_data:
        return

    headers, rows = table_data

    # Calculate dimensions
    num_rows = len(rows) + 1  # +1 for header
    num_cols = len(headers)

    # Position and size - align with content textbox
    left = Inches(0.5)
    top = Inches(1.5)
    width = Inches(9.0)
    height = Inches(3.5)

    # Create table
    shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
    table = shape.table

    # Set column widths
    col_width = width / num_cols
    for col_idx in range(num_cols):
        table.columns[col_idx].width = int(col_width)

    # Fill header row with bold text
    for col_idx, header_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = header_text
        for paragraph in cell.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.bold = True
                run.font.name = DEFAULT_FONT

    # Fill data rows
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_text in enumerate(row_data):
            if col_idx < num_cols:  # Handle inconsistent column counts
                cell = table.cell(row_idx + 1, col_idx)
                cell.text = cell_text
                # Apply font to cell content
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.name = DEFAULT_FONT


def add_paragraphs(text_frame, content):
    """Add paragraph text to text frame"""
    text_frame.word_wrap = True
    set_margins(text_frame)

    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    if not paragraphs:
        paragraphs = [l.strip() for l in content.split('\n') if l.strip()]
    if not paragraphs:
        return

    BLACK = RGBColor(0, 0, 0)

    for idx, para_text in enumerate(paragraphs):
        p = text_frame.paragraphs[0] if idx == 0 else text_frame.add_paragraph()
        apply_formatting(p, para_text, BLACK)


def add_content_to_textframe(text_frame, content):
    """Detect content type and add to text frame (bullets or paragraphs)"""
    if re.search(r'^\s*[-*+]\s', content, re.MULTILINE):
        add_bullets(text_frame, content)
    else:
        add_paragraphs(text_frame, content)


# ============================================================================
# SLIDE CREATION FUNCTIONS
# ============================================================================

def create_slide(prs, layout_idx, title, content, notes):
    """
    Create slide with specified layout
    Layout 0: Title slide
    Layout 1: Title and content
    Layout 2: Section header
    """
    slide = prs.slides.add_slide(prs.slide_layouts[layout_idx])

    # Set title
    if title and slide.shapes.title:
        title_shape = slide.shapes.title
        title_frame = title_shape.text_frame

        # Set text
        title_shape.text = title

        # Determine title font size based on layout
        if layout_idx == 0:
            title_size = Pt(44)  # Title slide
        else:
            title_size = Pt(32)  # Content and section slides

        # Apply formatting to text
        for paragraph in title_frame.paragraphs:
            paragraph.font.size = title_size
            paragraph.space_before = Pt(0)
            paragraph.space_after = Pt(0)
            paragraph.line_spacing = 1.0
            for run in paragraph.runs:
                run.font.color.rgb = SMOKY_BLUE
                run.font.name = DEFAULT_FONT
                run.font.bold = True  # Bold for all titles
                run.font.size = title_size

        # Configure text frame properties
        title_frame.word_wrap = False  # Don't wrap titles
        title_frame.vertical_anchor = MSO_ANCHOR.TOP

        # Match content margins for consistency
        title_frame.margin_left = Inches(0.05)
        title_frame.margin_top = Inches(0.025)
        title_frame.margin_right = Inches(0.05)
        title_frame.margin_bottom = Inches(0.025)

        # Position title based on layout
        if layout_idx in [0, 2]:  # Title slide and section slides - center the title
            title_shape.top = Inches(1.2)
            title_shape.left = Inches(0.5)
            title_shape.width = Inches(9.0)
            title_shape.height = Inches(1.0)
            title_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        else:  # Content slides - align left at top
            title_shape.left = Inches(0.3)
            title_shape.width = Inches(9.4)
            title_shape.height = Inches(0.5)

    # Add content for content slides (layout 1)
    if layout_idx == 1 and content:
        try:
            # Hide default placeholder to avoid "Click to add text"
            if len(slide.placeholders) > 1:
                slide.placeholders[1].width = 0
                slide.placeholders[1].height = 0

            # Check if table
            is_table = '|' in content and content.count('|') > 2
            if is_table:
                table_lines = [l for l in content.split('\n') if l.strip().startswith('|')]
                if len(table_lines) >= 2:
                    add_table(slide, content)
                    return slide

            # Create textbox for bullets/paragraphs
            content_box = slide.shapes.add_textbox(
                Inches(0.3), Inches(0.85),
                Inches(9.4), Inches(4.65)
            )
            add_content_to_textframe(content_box.text_frame, content)
        except Exception as e:
            print(f"⚠ Warning: Could not add content to slide: {e}")

    # Handle title slide content (layout 0)
    if layout_idx == 0 and content and len(slide.placeholders) > 1:
        try:
            subtitle_placeholder = slide.placeholders[1]
            subtitle_frame = subtitle_placeholder.text_frame
            set_margins(subtitle_frame)
            subtitle_placeholder.text = content

            # Position subtitle closer to title
            subtitle_placeholder.top = Inches(2.5)
            subtitle_placeholder.left = Inches(1.5)
            subtitle_placeholder.width = Inches(7.0)
            subtitle_placeholder.height = Inches(1.5)

            # Apply Heebo font to subtitle
            for paragraph in subtitle_frame.paragraphs:
                for run in paragraph.runs:
                    run.font.name = DEFAULT_FONT
        except Exception as e:
            print(f"⚠ Warning: Could not add subtitle: {e}")

    # Add speaker notes
    if notes:
        try:
            slide.notes_slide.notes_text_frame.text = notes
        except Exception as e:
            print(f"⚠ Warning: Could not add notes: {e}")

    return slide


# ============================================================================
# MAIN CONVERTER
# ============================================================================

def convert_markdown_to_pptx(markdown_file, output_file):
    """Main conversion function"""
    print(f"Reading markdown file: {markdown_file}")

    # Read markdown
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return False

    # Create presentation with standard Widescreen 16:9 preset
    prs = Presentation()
    prs.slide_width = Inches(10)      # Standard Widescreen 16:9
    prs.slide_height = Inches(5.625)  # Recognized as preset by PowerPoint/Google Slides

    # Split into slides
    slides_raw = split_slides(markdown_content)
    print(f"Found {len(slides_raw)} slides")

    # Process each slide
    for idx, slide_content in enumerate(slides_raw):
        # Skip empty slides
        if not slide_content.strip():
            continue

        try:
            # Extract components
            content, notes = extract_notes(slide_content)
            title, body = extract_title(content)

            # Determine layout
            layout = determine_layout(idx, title, body)

            # Debug output
            layout_names = {0: "Title", 1: "Content", 2: "Section"}
            print(f"  Slide {idx + 1}: {layout_names[layout]} - '{title[:50]}...'")

            # Create slide
            create_slide(prs, layout, title, body, notes)

        except Exception as e:
            print(f"⚠ Warning: Error processing slide {idx + 1}: {e}")
            continue

    # Save presentation
    try:
        prs.save(output_file)
        print(f"✓ Presentation saved: {output_file}")
        print(f"✓ Total slides: {len(prs.slides)}")
        return True
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return False


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Convert markdown to PowerPoint presentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example markdown format:

# Title Slide
Subtitle text
Author name

---

## Section One

---

## Content Slide
- Bullet point one
- Bullet point two with **bold** and *italic*
- Code example: `print("hello")`

<!-- Notes: These are speaker notes -->

---

## Table Example
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

---

## Section Two
"""
    )

    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', '--output', required=True, help='Output PPTX file')

    args = parser.parse_args()

    # Convert
    success = convert_markdown_to_pptx(args.input, args.output)

    # Exit with appropriate code
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
