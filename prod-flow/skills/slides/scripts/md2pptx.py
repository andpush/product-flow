#!/usr/bin/env python3
"""
Universal Markdown to PowerPoint Converter

Converts markdown files with --- slide separators into PPTX presentations.
Supports speaker notes, tables, bullets, links, and inline formatting.
"""

import re
import argparse
from markdown_it import MarkdownIt
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import MSO_ANCHOR
from pptx.dml.color import RGBColor

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULT_FONT = "Heebo"
ACCENT_COLOR = RGBColor(0x36, 0x4F, 0x6B)  # Smoky blue for titles, bold, italic, links
TEXT_COLOR = RGBColor(0, 0, 0)              # Black for regular text
MD_PARSER = MarkdownIt('commonmark', {'breaks': True, 'html': True}).enable('table')

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


def get_plain_text_from_tokens(tokens):
    """Extracts plain text from a token stream, preserving basic structure."""
    text_lines = []
    for token in tokens:
        if token.type == 'inline':
            text_lines.append(token.content)
        elif token.type == 'paragraph_close':
            text_lines.append('\n')
    return "".join(text_lines).strip()


def parse_slide_content(content):
    """
    Parses markdown content of a single slide into a title and a list of content blocks.
    """
    title = ""
    tokens = MD_PARSER.parse(content)
    body_tokens = tokens

    # Find the first h1 or h2 to use as a title
    for i, token in enumerate(tokens):
        if token.type == 'heading_open' and token.tag in ['h1', 'h2']:
            title_token = tokens[i + 1]
            if title_token.type == 'inline':
                title = title_token.content.strip()
                
                # Find the end of the heading block to slice tokens
                end_of_heading_index = i
                while tokens[end_of_heading_index].type != 'heading_close':
                    end_of_heading_index += 1
                
                body_tokens = tokens[end_of_heading_index + 1:]
                break # Stop after finding the first title
    
    body_content = get_plain_text_from_tokens(body_tokens)
    return title, body_content, body_tokens


def determine_layout(slide_index, title, content):
    """
    Determine slide layout based on content
    Returns: 0 (title), 1 (content), or 2 (section)
    """
    if slide_index == 0 and len(content.split('\\n')) <= 3:
        return 0
    if not content.strip():
        return 2
    return 1


# ============================================================================
# CONTENT ADDITION FUNCTIONS
# ============================================================================

def set_margins(text_frame):
    """Set reduced margins for text frames."""
    text_frame.margin_left = Inches(0.05)
    text_frame.margin_right = Inches(0.05)
    text_frame.margin_top = Inches(0.025)
    text_frame.margin_bottom = Inches(0.025)


def apply_inline_formatting(paragraph, inline_token):
    """Apply markdown inline formatting from markdown-it tokens."""
    if not inline_token.children:
        paragraph.text = inline_token.content
        return

    # Use a stack to manage nested styles (bold, italic)
    style_stack = []

    for child in inline_token.children:
        run = paragraph.add_run()
        run.text = child.content
        run.font.name = DEFAULT_FONT
        run.font.color.rgb = TEXT_COLOR
        
        if child.type == 'strong_open':
            style_stack.append('bold')
        elif child.type == 'em_open':
            style_stack.append('italic')
        elif child.type == 'strong_close' and 'bold' in style_stack:
            style_stack.remove('bold')
        elif child.type == 'em_close' and 'italic' in style_stack:
            style_stack.remove('italic')
        elif child.type == 'code_inline':
            run.font.name = 'Courier New'
            run.font.size = Pt(14)
        elif child.type == 'link_open':
            run.font.color.rgb = ACCENT_COLOR
            run.font.underline = True
            run.hyperlink.address = child.attrs['href']
        
        # Apply current styles from stack
        if 'bold' in style_stack:
            run.font.bold = True
            run.font.color.rgb = ACCENT_COLOR
        if 'italic' in style_stack:
            run.font.italic = True
            run.font.color.rgb = ACCENT_COLOR


def add_content_from_tokens(slide, content_box, tokens):
    """Iterates through markdown-it tokens and adds content to the slide."""
    text_frame = content_box.text_frame
    text_frame.word_wrap = True
    set_margins(text_frame)
    if text_frame.text: # Clear default text
        p = text_frame.paragraphs[0]
        p.clear()

    list_level = -1
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.type == 'paragraph_open':
            p = text_frame.add_paragraph()
            if list_level >= 0:
                p.level = list_level
            
            inline_token = tokens[i+1]
            if inline_token.type == 'inline':
                apply_inline_formatting(p, inline_token)
            i += 2 # Skip inline token
        elif token.type in ['bullet_list_open', 'ordered_list_open']:
            list_level += 1
        elif token.type in ['bullet_list_close', 'ordered_list_close']:
            list_level -= 1
        
        i += 1


def parse_table_from_tokens(tokens):
    headers, rows = [], []
    in_header, in_body, current_row = False, False, []

    for token in tokens:
        if token.type == 'table_close': break
        if token.type == 'thead_open': in_header = True
        elif token.type == 'thead_close': in_header = False
        elif token.type == 'tbody_open': in_body = True
        elif token.type == 'tbody_close': in_body = False
        elif token.type == 'tr_open': current_row = []
        elif token.type == 'tr_close':
            if in_header: headers = current_row
            elif in_body: rows.append(current_row)
        elif token.type == 'inline': current_row.append(token.content)
            
    return headers, rows


def add_table_shape(slide, headers, rows):
    if not headers: return
    num_rows, num_cols = len(rows) + 1, len(headers)
    # Align with the standard content placeholder position
    left, top = Inches(0.3), Inches(0.85)
    width, height = Inches(9.4), Inches(4.8)
    
    shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
    table = shape.table
    
    # Set column widths
    for c in range(num_cols): table.columns[c].width = int(width / num_cols)

    # Set minimal row height for all rows
    for r in range(num_rows):
        table.rows[r].height = Inches(0.4)
        
    # Populate header
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        for p in cell.text_frame.paragraphs:
            for run in p.runs: run.font.bold, run.font.name = True, DEFAULT_FONT
                
    # Populate data rows
    for r, row_data in enumerate(rows):
        for c, cell_text in enumerate(row_data):
            if c < num_cols:
                cell = table.cell(r + 1, c)
                cell.text = cell_text
                for p in cell.text_frame.paragraphs:
                    # Set vertical alignment for cell text
                    p.alignment = MSO_ANCHOR.MIDDLE
                    for run in p.runs: run.font.name = DEFAULT_FONT

# ============================================================================
# SLIDE CREATION FUNCTIONS
# ============================================================================

def remove_shape(slide, shape_to_remove):
    """Removes a shape from a slide."""
    sp = shape_to_remove.element
    sp.getparent().remove(sp)

def create_slide(prs, layout_idx, title, body_content, body_tokens, notes):
    """Create slide with specified layout."""
    slide = prs.slides.add_slide(prs.slide_layouts[layout_idx])

    if title and slide.shapes.title:
        title_shape = slide.shapes.title
        title_frame = title_shape.text_frame
        title_shape.text = title
        title_size = Pt(44) if layout_idx == 0 else Pt(32)
        for p in title_frame.paragraphs:
            p.font.size, p.line_spacing = title_size, 1.0
            p.space_before, p.space_after = Pt(0), Pt(0)
            for run in p.runs:
                run.font.color.rgb = ACCENT_COLOR
                run.font.name, run.font.bold, run.font.size = DEFAULT_FONT, True, title_size
        title_frame.word_wrap, title_frame.vertical_anchor = False, MSO_ANCHOR.TOP
        set_margins(title_frame)
        if layout_idx in [0, 2]:
            title_shape.top, title_shape.left, title_shape.width, title_shape.height = Inches(1.2), Inches(0.5), Inches(9.0), Inches(1.0)
            title_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        else:
            title_shape.left, title_shape.width, title_shape.height = Inches(0.3), Inches(9.4), Inches(0.5)

    is_table_slide = any(t.type == 'table_open' for t in body_tokens)
    
    if layout_idx == 1 and body_content:
        content_placeholder = None
        for shape in slide.placeholders:
            if shape.placeholder_format.idx in [1, 14]:
                content_placeholder = shape
                break
        
        if is_table_slide:
            headers, rows = parse_table_from_tokens(body_tokens)
            add_table_shape(slide, headers, rows)
            if content_placeholder:
                remove_shape(slide, content_placeholder)
        else:
            if content_placeholder:
                content_placeholder.left, content_placeholder.top = Inches(0.3), Inches(0.85)
                content_placeholder.width, content_placeholder.height = Inches(9.4), Inches(4.8)
            else:
                content_placeholder = slide.shapes.add_textbox(Inches(0.3), Inches(0.85), Inches(9.4), Inches(4.8))
            add_content_from_tokens(slide, content_placeholder, body_tokens)

    elif layout_idx == 0 and body_content and len(slide.placeholders) > 1:
        subtitle = slide.placeholders[1]
        set_margins(subtitle.text_frame)
        subtitle.text = body_content
        subtitle.top, subtitle.left, subtitle.width, subtitle.height = Inches(2.5), Inches(1.5), Inches(7.0), Inches(1.5)
        for p in subtitle.text_frame.paragraphs:
            for run in p.runs: run.font.name = DEFAULT_FONT

    if notes:
        slide.notes_slide.notes_text_frame.text = notes

    return slide

# ============================================================================
# MAIN CONVERTER
# ============================================================================

def convert_markdown_to_pptx(markdown_file, output_file):
    """Main conversion function"""
    print(f"Reading markdown file: {markdown_file}")
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return False

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(10), Inches(5.625)
    slides_raw = split_slides(markdown_content)
    print(f"Found {len(slides_raw)} slides")

    for idx, slide_content in enumerate(slides_raw):
        if not slide_content.strip(): continue
        try:
            content, notes = extract_notes(slide_content)
            title, body, body_tokens = parse_slide_content(content)
            layout = determine_layout(idx, title, body)
            layout_names = {0: "Title", 1: "Content", 2: "Section"}
            print(f"  Slide {idx + 1}: {layout_names[layout]} - '{title[:50]}...'")
            create_slide(prs, layout, title, body, body_tokens, notes)
        except Exception as e:
            print(f"⚠ Warning: Error processing slide {idx + 1}: {e}")
            import traceback
            traceback.print_exc()
            continue
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
        epilog="""...omitted for brevity...""")
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', '--output', required=True, help='Output PPTX file')
    args = parser.parse_args()
    success = convert_markdown_to_pptx(args.input, args.output)
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
