"""
Build all slide decks for the UCL AI Agents seminar.

Generates four PDFs (one per section) using reportlab.
Fonts: Merriweather Sans (Regular + Bold) from fonts/ directory.

Usage:
    python build_slides.py
"""

import os

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, "fonts")

# 16:9 at 72 dpi
W, H = 1280, 720

# Colours
BLACK = HexColor("#1A1A1A")
WHITE = HexColor("#FFFFFF")
ACCENT = HexColor("#2D5F8A")
LIGHT_GREY = HexColor("#F5F5F5")
MID_GREY = HexColor("#E0E0E0")

# Margins
MARGIN = 80
CONTENT_W = W - 2 * MARGIN

# Font sizes
TITLE_SIZE = 36
BODY_SIZE = 24
CODE_SIZE = 18
SMALL_SIZE = 18

# Line spacing multiplier
LINE_SPACING = 1.4


# ---------------------------------------------------------------------------
# Font registration
# ---------------------------------------------------------------------------

def register_fonts():
    pdfmetrics.registerFont(TTFont("MerriSans", os.path.join(FONT_DIR, "MerriweatherSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("MerriSans-Bold", os.path.join(FONT_DIR, "MerriweatherSans-Bold.ttf")))


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------

def new_slide(c, title_slide=False, first=False):
    """Start a new page with white background and accent bar."""
    if not first:
        c.showPage()
    c.setPageSize((W, H))

    # White background
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Accent bar at top
    bar_h = 6 if not title_slide else 8
    c.setFillColor(ACCENT)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)


def draw_title(c, text, y=None, size=TITLE_SIZE, color=BLACK, align="left"):
    """Draw a heading in Merriweather Sans Bold."""
    c.setFont("MerriSans-Bold", size)
    c.setFillColor(color)
    if y is None:
        y = H - MARGIN - 40
    if align == "center":
        c.drawCentredString(W / 2, y, text)
    else:
        c.drawString(MARGIN, y, text)
    return y


def draw_body(c, lines, start_y, size=BODY_SIZE, color=BLACK, font="MerriSans",
              indent=0, line_spacing=None):
    """Draw body text, one line per entry. Returns y after last line."""
    if line_spacing is None:
        line_spacing = size * LINE_SPACING
    c.setFont(font, size)
    c.setFillColor(color)
    y = start_y
    for line in lines:
        c.drawString(MARGIN + indent, y, line)
        y -= line_spacing
    return y


def draw_body_centered(c, lines, start_y, size=BODY_SIZE, color=BLACK,
                       font="MerriSans", line_spacing=None):
    """Draw body text centered horizontally."""
    if line_spacing is None:
        line_spacing = size * LINE_SPACING
    c.setFont(font, size)
    c.setFillColor(color)
    y = start_y
    for line in lines:
        c.drawCentredString(W / 2, y, line)
        y -= line_spacing
    return y


def draw_code_block(c, lines, start_y, width=None):
    """Draw a code block with light grey background and accent left border."""
    if width is None:
        width = CONTENT_W
    line_h = CODE_SIZE * 1.5
    block_h = len(lines) * line_h + 20
    x = MARGIN
    top_y = start_y + CODE_SIZE + 5

    # Background
    c.setFillColor(LIGHT_GREY)
    c.roundRect(x, top_y - block_h, width, block_h, 6, fill=1, stroke=0)

    # Left accent border
    c.setFillColor(ACCENT)
    c.rect(x, top_y - block_h, 4, block_h, fill=1, stroke=0)

    # Code text
    c.setFont("Courier", CODE_SIZE)
    c.setFillColor(BLACK)
    y = start_y
    for line in lines:
        c.drawString(x + 20, y, line)
        y -= line_h

    return top_y - block_h - 10


def draw_box(c, x, y, w, h, label, fill=None, stroke=ACCENT, radius=8):
    """Draw a rounded rectangle with a centred label."""
    if fill:
        c.setFillColor(fill)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)

    c.setStrokeColor(stroke)
    c.setLineWidth(2)
    c.roundRect(x, y, w, h, radius, fill=0, stroke=1)

    c.setFont("MerriSans", BODY_SIZE)
    c.setFillColor(BLACK)
    text_w = c.stringWidth(label, "MerriSans", BODY_SIZE)
    c.drawString(x + (w - text_w) / 2, y + (h - BODY_SIZE) / 2 + 4, label)


def draw_arrow(c, x1, y1, x2, y2, label=None, color=ACCENT):
    """Draw an arrow with optional label above it."""
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.line(x1, y1, x2, y2)

    # Arrowhead
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    head_len = 12
    c.line(x2, y2,
           x2 - head_len * math.cos(angle - 0.4),
           y2 - head_len * math.sin(angle - 0.4))
    c.line(x2, y2,
           x2 - head_len * math.cos(angle + 0.4),
           y2 - head_len * math.sin(angle + 0.4))

    if label:
        c.setFont("MerriSans", SMALL_SIZE)
        c.setFillColor(BLACK)
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        c.drawCentredString(mid_x, mid_y + 14, label)


# ---------------------------------------------------------------------------
# Section 01: Stateless Nondeterministic Function
# ---------------------------------------------------------------------------

def build_section_01():
    path = os.path.join(BASE_DIR, "01-stateless-nondeterministic-function", "slides.pdf")
    c = Canvas(path, pagesize=(W, H))

    # -- Slide 1: Title --
    new_slide(c, title_slide=True, first=True)
    draw_title(c, "What is an LLM?", y=H / 2 + 60, size=44, align="center")
    draw_body_centered(c, ["A reductive account for physicists"], H / 2 - 10, size=BODY_SIZE)
    draw_body_centered(c, ["Tobias J. Osborne"], H / 2 - 80, size=SMALL_SIZE,
                       color=HexColor("#666666"))

    # -- Slide 2: The observable interface --
    new_slide(c)
    draw_title(c, "The observable interface")
    y = H - MARGIN - 100
    draw_code_block(c, ["f : String -> String"], y)
    y -= 100
    draw_body(c, [
        "From outside the API boundary, this is the entire",
        "observable behaviour. No hidden state is carried",
        "between calls.",
    ], y)

    # -- Slide 3: Stateless --
    new_slide(c)
    draw_title(c, "Stateless")
    box_y = H / 2 - 20
    box_w, box_h = 200, 80
    draw_box(c, 200, box_y, box_w, box_h, "Call 1")
    draw_box(c, 680, box_y, box_w, box_h, "Call 2")

    # Arrows in/out of each box
    draw_arrow(c, 120, box_y + box_h / 2, 200, box_y + box_h / 2)
    draw_arrow(c, 400, box_y + box_h / 2, 480, box_y + box_h / 2)
    draw_arrow(c, 600, box_y + box_h / 2, 680, box_y + box_h / 2)
    draw_arrow(c, 880, box_y + box_h / 2, 960, box_y + box_h / 2)

    draw_body_centered(c, [
        "Each evaluation is independent.",
        "The function has no memory of previous calls.",
    ], box_y - 60)

    # -- Slide 4: Nondeterministic --
    new_slide(c)
    draw_title(c, "Nondeterministic")
    # One input box on left, three output boxes on right
    # Position everything higher to leave room for text below
    center_y = H / 2 + 40
    in_x = 150
    in_y = center_y - 30
    draw_box(c, in_x, in_y, 220, 60, '"What is spin?"')

    out_labels = ['"Spin is..."', '"Angular..."', '"In QM..."']
    for i, label in enumerate(out_labels):
        out_y = center_y + 70 - i * 80
        draw_box(c, 700, out_y, 220, 60, label)
        draw_arrow(c, in_x + 220, in_y + 30, 700, out_y + 30)

    draw_body(c, [
        "The model samples from a learned conditional distribution",
        "P(next token | preceding tokens).",
    ], center_y - 140)

    # -- Slide 5: Temperature --
    new_slide(c)
    draw_title(c, "Temperature")
    y = H - MARGIN - 110
    draw_code_block(c, [
        "P(token_i) = exp(logit_i / T) / sum_j exp(logit_j / T)",
    ], y)
    y -= 100
    draw_body(c, [
        "T -> 0: greedy (ground state).",
        "T -> infinity: uniform (infinite temperature).",
        "",
        "Direct analogy to the Boltzmann distribution.",
    ], y)

    # -- Slide 6: Tokens --
    new_slide(c)
    draw_title(c, "Tokens")
    y = H - MARGIN - 100
    draw_body(c, [
        "The discretisation of language. Not characters.",
        "Not words. Subword chunks from a fixed vocabulary",
        "V of ~100k entries.",
    ], y)
    y -= 120
    draw_code_block(c, [
        "'theoretical physics' -> ['theor', 'etical', ' physics']",
    ], y)

    # -- Slide 7: Inference --
    new_slide(c)
    draw_title(c, "Inference")
    y = H - MARGIN - 100
    draw_body(c, [
        "One forward pass through a neural network with",
        "fixed weights. No learning occurs. No state is",
        "mutated. The model is a frozen function being",
        "evaluated.",
    ], y)

    # -- Slide 8: Summary --
    new_slide(c)
    draw_title(c, "Summary")
    y = H - MARGIN - 100
    draw_body(c, [
        "An LLM is a stateless nondeterministic function",
        "",
        "    f : String -> String",
        "",
        "that samples from P(next_token | context) via a",
        "single forward pass through a frozen neural network.",
    ], y)

    c.save()
    print(f"  Built {path}")


# ---------------------------------------------------------------------------
# Section 02: Illusion of Chat
# ---------------------------------------------------------------------------

def build_section_02():
    path = os.path.join(BASE_DIR, "02-illusion-of-chat", "slides.pdf")
    c = Canvas(path, pagesize=(W, H))

    # -- Slide 1: Title --
    new_slide(c, title_slide=True, first=True)
    draw_title(c, "The illusion of chat and memory", y=H / 2 + 20, size=40,
               align="center")

    # -- Slide 2: A single API call --
    new_slide(c)
    draw_title(c, "A single API call")
    box_y = H / 2 - 20
    draw_box(c, 150, box_y, 200, 70, "Client")
    draw_box(c, 700, box_y, 200, 70, "API")
    draw_arrow(c, 350, box_y + 50, 700, box_y + 50, label="prompt (string)")
    draw_arrow(c, 700, box_y + 20, 350, box_y + 20, label="completion (string)")
    draw_body_centered(c, [
        "One string in. One string out.",
        "That is the entire interaction.",
    ], box_y - 50)

    # -- Slide 3: The HTTP reality --
    new_slide(c)
    draw_title(c, "The HTTP reality")
    y = H - MARGIN - 110
    draw_code_block(c, [
        'POST /v1/messages',
        '{',
        '  "model": "claude-sonnet-4-20250514",',
        '  "messages": [',
        '    {"role": "user",',
        '     "content": "What is a quark?"}',
        '  ]',
        '}',
    ], y)

    # -- Slide 4: How chat works --
    new_slide(c)
    draw_title(c, "How chat works")
    y = H - MARGIN - 110
    draw_code_block(c, [
        "Turn 1: [user_1]",
        "Turn 2: [user_1, assistant_1, user_2]",
        "Turn 3: [user_1, assistant_1, user_2, assistant_2, user_3]",
    ], y)
    y -= 100
    draw_body(c, [
        "The client re-sends the ENTIRE history every time.",
        "The LLM has no memory. The client maintains the illusion.",
    ], y)

    # -- Slide 5: The context window --
    new_slide(c)
    draw_title(c, "The context window")
    y = H - MARGIN - 100
    draw_body(c, [
        "The input has a maximum length in tokens.",
        "This is the fundamental constraint. When the",
        "conversation exceeds it, something must be dropped.",
    ], y)
    y -= 120
    draw_body(c, [
        "Typical context windows: 8k, 128k, 200k tokens.",
    ], y, font="MerriSans-Bold")

    # -- Slide 6: The system prompt --
    new_slide(c)
    draw_title(c, "The system prompt")
    y = H - MARGIN - 100
    draw_body(c, [
        "A hidden preamble prepended to every call.",
        "You never see it in chat UIs. It shapes",
        "behaviour, persona, and constraints.",
        "",
        "It is just more text.",
    ], y)

    # -- Slide 7: Summary --
    new_slide(c)
    draw_title(c, "Summary")
    y = H - MARGIN - 100
    draw_body(c, [
        "Every chat interaction is a fresh, independent",
        "function evaluation on an ever-growing input string.",
        "",
        "There is no persistent state on the server.",
        "",
        "Chat is a loop.",
        "Memory is an illusion maintained by the client.",
    ], y)

    c.save()
    print(f"  Built {path}")


# ---------------------------------------------------------------------------
# Section 03: Primitive Agent
# ---------------------------------------------------------------------------

def build_section_03():
    path = os.path.join(BASE_DIR, "03-primitive-agent", "slides.pdf")
    c = Canvas(path, pagesize=(W, H))

    # -- Slide 1: Title --
    new_slide(c, title_slide=True, first=True)
    draw_title(c, "From function to agent", y=H / 2 + 20, size=44,
               align="center")

    # -- Slide 2: The agent loop --
    new_slide(c)
    draw_title(c, "The agent loop")
    y = H - MARGIN - 110
    draw_code_block(c, [
        "while not done:",
        "    response = llm(system_prompt + history)",
        "    tool_calls = parse(response)",
        "    results = execute(tool_calls)",
        "    history += [response, results]",
    ], y)
    y -= 120
    draw_body(c, [
        "This is the complete architecture of every coding agent.",
    ], y, font="MerriSans-Bold")

    # -- Slide 3: Tool definition --
    new_slide(c)
    draw_title(c, "Tool definition")
    y = H - MARGIN - 100
    draw_body(c, [
        "You describe available tools in the system prompt.",
        "The LLM generates structured text requesting a",
        "tool call. Your scaffolding parses and executes it.",
        "",
        "The LLM never executes anything.",
    ], y)

    # -- Slide 4: Our agent: two tools --
    new_slide(c)
    draw_title(c, "Our agent: two tools")
    y = H - MARGIN - 110
    draw_code_block(c, [
        "read_file(path) -> contents",
        "write_file(path, content) -> ok",
    ], y)
    y -= 80
    draw_body(c, [
        "That is enough to do useful work.",
    ], y, font="MerriSans-Bold")

    # -- Slide 5: What Claude Code, Cursor, Copilot actually are --
    new_slide(c)
    draw_title(c, "What Claude Code, Cursor, Copilot actually are")
    y = H - MARGIN - 100
    draw_body(c, [
        "The same loop. More tools. Better prompts.",
        "",
        "The fundamental mechanism is identical.",
    ], y)

    # -- Slide 6: Live demo --
    new_slide(c)
    draw_title(c, "Live demo", y=H / 2 + 20, size=44, align="center")
    draw_body_centered(c, ["Let us watch the agent work."], H / 2 - 40)

    c.save()
    print(f"  Built {path}")


# ---------------------------------------------------------------------------
# Section 04: Audience Vote
# ---------------------------------------------------------------------------

def build_section_04():
    path = os.path.join(BASE_DIR, "04-audience-vote", "slides.pdf")
    c = Canvas(path, pagesize=(W, H))

    # -- Slide 1: Title --
    new_slide(c, title_slide=True, first=True)
    draw_title(c, "What should we try?", y=H / 2 + 40, size=44,
               align="center")
    draw_body_centered(c, ["Vote."], H / 2 - 30, size=36,
                       font="MerriSans-Bold")

    # -- Options --
    options = [
        ("Option 1: LaTeX lint",
         ["Parse a .tex file. Find every undefined \\ref",
          "and \\cite. Report what is broken."]),
        ("Option 2: Data to figure",
         ["Read a CSV. Fit a power law. Generate a",
          "publication-quality plot with error bars.",
          "Save as PDF."]),
        ("Option 3: DOI to BibTeX",
         ["Given a list of DOIs, fetch metadata, produce",
          "a consistently formatted .bib file."]),
        ("Option 4: Seminar to calendar",
         ["Scrape a seminar schedule from a URL.",
          "Produce an .ics calendar file."]),
        ("Option 5: Batch rename",
         ["I describe a naming convention in English.",
          "The agent renames 200 files to match."]),
        ("Option 6: Dimensional analysis",
         ["Read a paper draft. Check that every equation",
          "is dimensionally consistent."]),
    ]

    for title, lines in options:
        new_slide(c)
        draw_title(c, title)
        y = H - MARGIN - 100
        draw_body(c, lines, y)

    # -- Slide 8: Raise your hand --
    new_slide(c)
    draw_title(c, "Raise your hand.", y=H / 2 + 20, size=44, align="center")

    c.save()
    print(f"  Built {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    register_fonts()
    print("Building slides...")
    build_section_01()
    build_section_02()
    build_section_03()
    build_section_04()
    print("Done. All slides built.")


if __name__ == "__main__":
    main()
