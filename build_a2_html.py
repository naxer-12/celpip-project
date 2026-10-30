#!/usr/bin/env python3
"""
build_a2_html.py - Standalone HTML Generator for French A2 Learning Roadmap & Checklist

Generates French_Learning_Roadmap_Checklist_French_A2.html containing all 71 fully styled,
self-contained .newpage containers formatted to 902px x 1166px print dimensions.
All 193 WOFF2 fonts and 71 page background images are embedded as base64 data URIs.
"""

import os
import json
import base64
import html
from a2_curriculum_data import A2_PAGES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "scribd_raw", "fonts")
IMAGES_DIR = os.path.join(BASE_DIR, "scribd_raw", "images")
FONTS_METADATA_PATH = os.path.join(BASE_DIR, "scribd_fonts.json")
DEFAULT_OUTPUT_PATH = os.path.join(BASE_DIR, "French_Learning_Roadmap_Checklist_French_A2.html")


def load_fonts_css() -> str:
    """Load and base64-encode all 193 WOFF2 fonts and generate font-face rules."""
    with open(FONTS_METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    css_blocks = []
    class_mappings = []

    for entry in metadata:
        fid = entry["id"]
        family = entry["family"]
        fallback = entry["fallback"]
        weight = entry.get("weight", "normal")
        style = entry.get("style", "normal")
        font_path = os.path.join(FONTS_DIR, f"{fid}.woff2")

        if os.path.exists(font_path):
            with open(font_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            css_blocks.append(
                f'@font-face {{\n'
                f'  font-family: "{family}";\n'
                f'  src: url("data:font/woff2;base64,{b64}") format("woff2");\n'
                f'  font-weight: {weight};\n'
                f'  font-style: {style};\n'
                f'}}'
            )
            class_mappings.append(
                f'div.{family} span, .{family} span, div.{family}, .{family} {{ font-family: "{family}", {fallback} !important; }}'
            )

    return "\n".join(css_blocks) + "\n\n" + "\n".join(class_mappings)


def generate_kerning_css() -> str:
    """Generate scaled kerning and spacing rules .w1..w39 and .l1..l39."""
    rules = []
    for i in range(1, 40):
        w = round(0.2 * i, 1)
        rules.append(
            f'.text_layer span.w{i} {{ width: {w}px !important; display: inline-block !important; height: 1px !important; }}\n'
            f'.text_layer span.l{i} {{ margin: 0 0 0 -{w}px !important; display: inline !important; }}'
        )
    return "\n".join(rules)


def load_image_b64(page_num: int) -> str:
    """Load background image for page_num (1 uses 1_a2.jpg, 2-71 use {num}.jpg)."""
    if page_num == 1:
        img_path = os.path.join(IMAGES_DIR, "1_a2.jpg")
        if not os.path.exists(img_path):
            img_path = os.path.join(IMAGES_DIR, "1.jpg")
    else:
        img_path = os.path.join(IMAGES_DIR, f"{page_num}.jpg")

    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def format_text(text: str) -> str:
    """Format text for HTML, escaping tag characters while preserving readability and line breaks."""
    return text.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")


def render_page_content(data: dict) -> str:
    """Render the inner text layer HTML for a page based on its type."""
    p_num = data["page"]
    p_type = data.get("type", "checklist")
    title = format_text(data.get("title", ""))
    subtitle = format_text(data.get("subtitle", ""))
    intro = format_text(data.get("intro", ""))
    badge_num = data.get("badge_num", "")

    if p_type == "cover":
        return f"""<div class="ie_fix">
<div class="ff79" style="font-size:69.6px">
<span class="a" style="left:230.4px;top:131px;word-spacing:-0.2px;color:#313435;font-weight:bold;">French Learning </span><span class="a" style="left:172.8px;top:207.2px;word-spacing:0.2px;color:#313435;font-weight:bold;">Roadmap & Checklist</span></div>
<div class="ff79" style="font-size:46.4px">
<span class="a" style="left:367.4px;top:326.8px;word-spacing:0.2px;color:#ffffff;font-weight:bold;width:170px;text-align:center;">French A2</span></div>
</div>"""

    # Badge span for pages 2 to 71
    badge_html = ""
    if badge_num:
        badge_html = f'<div class="page-badge"><span class="a" style="left:811.6px;top:1116px;font-family:\'ff143\',Trebuchet MS,sans-serif;font-size:29.4px;font-weight:bold;color:#1a1a1a;">{badge_num}</span></div>'

    body_parts = []
    body_parts.append(f'<div class="page-title">{title}</div>')
    if subtitle:
        body_parts.append(f'<div class="page-subtitle">{subtitle}</div>')
    if intro:
        body_parts.append(f'<div class="page-intro">{intro}</div>')

    # Page Type Specific Layouts
    if p_type == "objectives":
        sections = data.get("sections", [])
        for sec in sections:
            sec_title = format_text(sec.get("title", ""))
            body_parts.append(f'<div class="section-title">{sec_title}</div>')
            for item in sec.get("items", []):
                body_parts.append(
                    f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                )

    elif p_type == "themes_table":
        # Page 4 has Real-Life Outcomes at top
        if p_num == 4 and "items" in data:
            for item in data["items"]:
                body_parts.append(
                    f'<div class="checklist-item"><span class="green-check">✓</span><span>{format_text(item)}</span></div>'
                )
            body_parts.append('<div class="section-title" style="margin-top:14px; margin-bottom:6px;">Core Themes &amp; Topics (Themes 1–4)</div>')

        table = data.get("table", {})
        headers = table.get("headers", [])
        rows = table.get("rows", [])
        body_parts.append('<table class="roadmap-table themes-table"><thead><tr>')
        widths = ["24%", "36%", "40%"]
        for idx, h in enumerate(headers):
            w_style = f' style="width:{widths[idx]}"' if idx < len(widths) else ""
            body_parts.append(f'<th{w_style}>{format_text(h)}</th>')
        body_parts.append('</tr></thead><tbody>')
        for row in rows:
            body_parts.append('<tr>')
            for cell in row:
                body_parts.append(f'<td>{format_text(cell)}</td>')
            body_parts.append('</tr>')
        body_parts.append('</tbody></table>')

    elif p_type == "functions_table":
        table = data.get("table", {})
        headers = table.get("headers", [])
        rows = table.get("rows", [])
        body_parts.append('<table class="roadmap-table functions-table"><thead><tr>')
        widths = ["28%", "32%", "40%"]
        for idx, h in enumerate(headers):
            w_style = f' style="width:{widths[idx]}"' if idx < len(widths) else ""
            body_parts.append(f'<th{w_style}>{format_text(h)}</th>')
        body_parts.append('</tr></thead><tbody>')
        for row in rows:
            body_parts.append('<tr>')
            for cell in row:
                body_parts.append(f'<td>{format_text(cell)}</td>')
            body_parts.append('</tr>')
        body_parts.append('</tbody></table>')

    elif p_type == "vocab_table":
        table = data.get("table", {})
        headers = table.get("headers", [])
        rows = table.get("rows", [])
        body_parts.append('<table class="roadmap-table vocab-table"><thead><tr>')
        widths = ["25%", "14%", "25%", "36%"]
        for idx, h in enumerate(headers):
            w_style = f' style="width:{widths[idx]}"' if idx < len(widths) else ""
            body_parts.append(f'<th{w_style}>{format_text(h)}</th>')
        body_parts.append('</tr></thead><tbody>')
        for row in rows:
            body_parts.append('<tr>')
            for cell in row:
                body_parts.append(f'<td>{format_text(cell)}</td>')
            body_parts.append('</tr>')
        body_parts.append('</tbody></table>')

    elif p_type == "audit":
        sections = data.get("sections", [])
        for sec in sections:
            sec_title = format_text(sec.get("title", ""))
            body_parts.append(f'<div class="section-title">{sec_title}</div>')
            for item in sec.get("items", []):
                body_parts.append(
                    f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                )
        if p_num == 71:
            body_parts.append(
                '<div class="readiness-box">'
                '<div class="readiness-title">🎉 CEFR B1 Transition Benchmark</div>'
                '<div class="readiness-text">If you have mastered and checked off at least 85–90% of the criteria across this roadmap: <strong>You are fully prepared to advance to French B1 (Intermediate)! Félicitations pour votre parcours !</strong></div>'
                '</div>'
            )

    else:  # checklist (Grammar Foundation & 4-Skills Mastery)
        sections = data.get("sections", [])
        for sec in sections:
            sec_title = format_text(sec.get("title", ""))
            body_parts.append(f'<div class="section-title">{sec_title}</div>')
            for item in sec.get("items", []):
                body_parts.append(
                    f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                )

    inner_content = "\n".join(body_parts)
    return f"""<div class="ie_fix">
<div class="content-container">
{inner_content}
</div>
{badge_html}
</div>"""


def build_html(output_path: str = None) -> str:
    """Generate the complete self-contained French A2 HTML document."""
    if output_path is None:
        output_path = DEFAULT_OUTPUT_PATH

    print("Loading and base64-encoding fonts...")
    fonts_css = load_fonts_css()
    kerning_css = generate_kerning_css()

    print("Building HTML pages 1 to 71...")
    pages_html = []

    for p_num in range(1, 72):
        data = A2_PAGES_DATA[p_num]
        img_b64 = load_image_b64(p_num)
        text_content = render_page_content(data)

        page_block = f"""<div class="newpage" id="page{p_num}" style="width: 902px; height:1166px">
<div class="text_layer" style="z-index:2">
{text_content}
</div>
<div class="image_layer" style="z-index: 1">
<div class="ie_fix">
<img class="absimg" src="data:image/jpeg;base64,{img_b64}">
</div>
</div>
</div>"""
        pages_html.append(page_block)

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>French Learning Roadmap & Checklist - French A2</title>
<style>
@page {{
  size: 902px 1166px;
  margin: 0;
}}
*, *:before, *:after {{
  box-sizing: border-box;
}}
html, body {{
  margin: 0 !important;
  padding: 0 !important;
  font-size: 0 !important;
  line-height: 0 !important;
  background-color: #ffffff;
  width: 902px;
}}
.newpage {{
  font-size: 16px;
  line-height: normal;
  width: 902px !important;
  height: 1166px !important;
  position: relative !important;
  page-break-inside: avoid !important;
  break-inside: avoid !important;
  page-break-after: always !important;
  break-after: page !important;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}}
.newpage:last-of-type {{
  page-break-after: auto !important;
  break-after: auto !important;
}}
.image_layer {{
  width: 902px !important;
  height: 1166px !important;
  overflow: hidden !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  z-index: 1 !important;
}}
.image_layer .absimg {{
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  width: 902px !important;
  height: 1166px !important;
  object-fit: fill !important;
  border: none !important;
}}
.text_layer {{
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 902px !important;
  height: 1166px !important;
  pointer-events: none !important;
  z-index: 2 !important;
  transform: none !important;
  transform-origin: unset !important;
}}
div[class*="ff"] {{
  display: block !important;
}}
span.a, span.g {{
  position: absolute !important;
  display: block !important;
}}

/* Base64 Embedded WOFF2 Fonts */
{fonts_css}

/* Scaled Kerning & Width Helpers */
{kerning_css}

/* Structural & Typography Styles */
.content-container {{
  position: absolute;
  left: 60px;
  top: 172px;
  width: 782px;
  pointer-events: auto;
  box-sizing: border-box;
  white-space: normal !important;
  line-height: normal !important;
}}
.content-container * {{
  white-space: normal;
  box-sizing: border-box;
}}
.page-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 24px;
  font-weight: bold;
  color: #1a1a1a;
  margin-bottom: 4px;
  line-height: 1.25;
}}
.page-subtitle {{
  font-family: "ff119", Arial, sans-serif;
  font-size: 14.5px;
  font-weight: bold;
  color: #1c528a;
  margin-bottom: 8px;
  line-height: 1.3;
}}
.page-intro {{
  font-family: "ff119", Arial, sans-serif;
  font-size: 13.5px;
  line-height: 1.45;
  color: #333333;
  margin-bottom: 14px;
}}
.section-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 16.5px;
  font-weight: bold;
  color: #1a1a1a;
  margin-top: 12px;
  margin-bottom: 8px;
  padding-bottom: 3px;
  border-bottom: 1.5px solid #eaeaea;
}}
.checklist-item {{
  display: flex;
  align-items: flex-start;
  margin-bottom: 8px;
  font-family: "ff119", Arial, sans-serif;
  font-size: 13.5px;
  line-height: 1.4;
  color: #222221;
}}
.custom-cb {{
  display: inline-block;
  width: 16px;
  height: 16px;
  min-width: 16px;
  border: 2px solid #48b3b6;
  border-radius: 4px;
  background: #ffffff;
  margin-right: 10px;
  margin-top: 2px;
}}
.green-check {{
  display: inline-block;
  width: 17px;
  height: 17px;
  min-width: 17px;
  line-height: 17px;
  text-align: center;
  border-radius: 50%;
  background: #74a866;
  color: #ffffff;
  font-size: 11px;
  font-weight: bold;
  margin-right: 10px;
  margin-top: 2px;
}}
table.roadmap-table {{
  width: 100%;
  border-collapse: collapse;
  border: 1.5px solid #1a1a1a;
  background: #ffffff;
  font-size: 12px;
  line-height: 1.35;
  margin-top: 6px;
}}
table.roadmap-table th {{
  background: #d1ecee;
  color: #1a1a1a;
  border: 1.5px solid #1a1a1a;
  padding: 6px 8px;
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-weight: bold;
  text-align: left;
}}
table.roadmap-table td {{
  border: 1.5px solid #1a1a1a;
  padding: 5px 8px;
  vertical-align: top;
  color: #222221;
  font-family: "ff119", Arial, sans-serif;
}}
table.vocab-table {{
  font-size: 11.5px;
}}
table.vocab-table td {{
  padding: 4px 6px;
}}
.readiness-box {{
  background: #f0fdf4;
  border: 2px solid #22c55e;
  border-radius: 8px;
  padding: 12px 16px;
  margin-top: 14px;
}}
.readiness-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 15px;
  font-weight: bold;
  color: #15803d;
  margin-bottom: 4px;
}}
.readiness-text {{
  font-family: "ff119", Arial, sans-serif;
  font-size: 13px;
  line-height: 1.4;
  color: #166534;
}}
.page-badge {{
  position: absolute;
  left: 811.6px;
  top: 1116px;
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 29.4px;
  font-weight: bold;
  color: #1a1a1a;
  text-align: center;
  pointer-events: none;
}}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>"""

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Generated {output_path} ({size_mb:.2f} MB, 71 pages)")
    return output_path


if __name__ == "__main__":
    build_html()
