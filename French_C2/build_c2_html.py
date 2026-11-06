#!/usr/bin/env python3
"""
build_c2_html.py - Standalone HTML Generator for French C2 Learning Roadmap & Checklist

Generates French_Learning_Roadmap_Checklist_French_C2.html containing all 71 fully styled,
self-contained .newpage containers formatted to 902px x 1166px print dimensions.
All 193 WOFF2 fonts and 71 page background images are embedded as base64 data URIs.
Brand Color: Midnight Indigo (#1e1b4b)
"""

import os
import json
import base64
import html
from c2_curriculum_data import C2_PAGES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "scribd_raw", "fonts")
if not os.path.exists(FONTS_DIR):
    FONTS_DIR = os.path.join(os.path.dirname(BASE_DIR), "scribd_raw", "fonts") if os.path.exists(os.path.join(BASE_DIR, "scribd_raw", "fonts")) else os.path.join(BASE_DIR, "..", "scribd_raw", "fonts")
IMAGES_DIR = os.path.join(BASE_DIR, "scribd_raw", "images")
if not os.path.exists(IMAGES_DIR):
    IMAGES_DIR = os.path.join(os.path.dirname(BASE_DIR), "scribd_raw", "images") if os.path.exists(os.path.join(BASE_DIR, "scribd_raw", "images")) else os.path.join(BASE_DIR, "..", "scribd_raw", "images")
FONTS_METADATA_PATH = os.path.join(BASE_DIR, "scribd_fonts.json")
if not os.path.exists(FONTS_METADATA_PATH):
    FONTS_METADATA_PATH = os.path.join(os.path.dirname(BASE_DIR), "scribd_fonts.json") if os.path.exists(os.path.join(BASE_DIR, "scribd_fonts.json")) else os.path.join(BASE_DIR, "..", "scribd_fonts.json")
DEFAULT_OUTPUT_PATH = os.path.join(BASE_DIR, "French_Learning_Roadmap_Checklist_French_C2.html")


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
    """Load background image for page_num (1 uses 1_c2.jpg, 2-71 use {num}.jpg)."""
    if page_num == 1:
        img_path = os.path.join(IMAGES_DIR, "1_c2.jpg")
        if not os.path.exists(img_path):
            img_path = os.path.join(IMAGES_DIR, "1.jpg")
    else:
        img_path = os.path.join(IMAGES_DIR, f"{page_num}.jpg")

    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def format_text(text: str) -> str:
    """Escape HTML entities while preserving line breaks."""
    return html.escape(text, quote=False).replace("\n", "<br>")


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
<!-- French Learning Roadmap & Checklist -->
<div class="ff79" style="font-size:69.6px">
<span class="a" style="left:230.4px;top:131px;word-spacing:-0.2px;color:#313435;font-weight:bold;">French Learning </span><span class="a" style="left:172.8px;top:207.2px;word-spacing:0.2px;color:#313435;font-weight:bold;">Roadmap &amp; Checklist</span></div>
<div class="ff79" style="font-size:46.4px">
<span class="a" style="left:367.4px;top:326.8px;word-spacing:0.2px;color:transparent;opacity:0;font-weight:bold;width:170px;text-align:center;">French C2</span></div>
</div>"""

    badge_html = ""
    if badge_num:
        badge_html = f'<div class="page-badge">{badge_num}</div>'

    body_parts = []
    body_parts.append(f'<div class="page-title">{title}</div>')
    if subtitle:
        body_parts.append(f'<div class="page-subtitle">{subtitle}</div>')
    if intro:
        body_parts.append(f'<div class="page-intro">{intro}</div>')

    if p_type == "outcomes":
        headers = data.get("table_headers", ["Theme", "Description", "Outcomes"])
        th_html = "".join(f"<th>{format_text(h)}</th>" for h in headers)
        rows_html = []
        for row in data.get("table_rows", []):
            cells = "".join(f"<td>{format_text(c)}</td>" for c in row)
            rows_html.append(f"<tr>{cells}</tr>")
        table_html = f"""<table class="outcomes-table">
<thead><tr>{th_html}</tr></thead>
<tbody>{"".join(rows_html)}</tbody>
</table>"""
        body_parts.append(table_html)

        footer_title = format_text(data.get("footer_title", "Real-Life Outcomes"))
        footer_items = data.get("footer_items", [])
        if footer_items:
            body_parts.append(f'<div class="footer-title">{footer_title}</div>')
            for item in footer_items:
                body_parts.append(
                    f'<div class="outcome-check-item"><span class="green-check">&#10003;</span><span>{format_text(item)}</span></div>'
                )

    elif p_type == "functions":
        headers = data.get("table_headers", ["Function", "Examples", "Use Context"])
        th_html = "".join(f"<th>{format_text(h)}</th>" for h in headers)
        rows_html = []
        for row in data.get("table_rows", []):
            cells = "".join(f"<td>{format_text(c)}</td>" for c in row)
            rows_html.append(f"<tr>{cells}</tr>")
        table_html = f"""<table class="functions-table">
<thead><tr>{th_html}</tr></thead>
<tbody>{"".join(rows_html)}</tbody>
</table>"""
        body_parts.append(table_html)

        footer_title = format_text(data.get("footer_title", "Key Communicative Goals"))
        footer_items = data.get("footer_items", [])
        if footer_items:
            body_parts.append(f'<div class="footer-title">{footer_title}</div>')
            for item in footer_items:
                body_parts.append(
                    f'<div class="outcome-check-item"><span class="green-check">&#10003;</span><span>{format_text(item)}</span></div>'
                )

    
    elif p_type == "resources":
        resources = data.get("resources", [])
        for res in resources:
            name = format_text(res.get("name", ""))
            badge = format_text(res.get("badge", ""))
            url = format_text(res.get("url", ""))
            what = format_text(res.get("what", ""))
            features = format_text(res.get("features", ""))
            focus = format_text(res.get("focus", ""))
            tips = format_text(res.get("tips", ""))
            body_parts.append(
                f'<div class="resource-card">\n'
                f'  <div class="resource-card-header">\n'
                f'    <span class="resource-name">{name}</span>\n'
                f'    <span class="resource-badge">{badge}</span>\n'
                f'  </div>\n'
                f'  <div class="resource-row"><span class="resource-label">Platform / URL:</span> <span class="resource-url">{url}</span></div>\n'
                f'  <div class="resource-row"><span class="resource-label">Content:</span> {what}</div>\n'
                f'  <div class="resource-row"><span class="resource-label">Key Features:</span> {features}</div>\n'
                f'  <div class="resource-row"><span class="resource-label">Focus:</span> {focus}</div>\n'
                f'  <div class="resource-row"><span class="resource-label">Study Routine:</span> {tips}</div>\n'
                f'  <div class="checklist-item" style="margin-top:6px; margin-bottom:0;"><span class="custom-cb"></span><span>Mark as active weekly study resource</span></div>\n'
                f'</div>'
            )

    elif p_type == "audit":
        sections = data.get("sections", [])
        if sections:
            for sec in sections:
                sec_title = format_text(sec.get("title", ""))
                body_parts.append(f'<div class="section-title">{sec_title}</div>')
                for item in sec.get("items", []):
                    body_parts.append(
                        f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                    )
        elif "items" in data:
            for item in data["items"]:
                body_parts.append(
                    f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                )

    else:  # checklist, grammar, thematic_vocab, speaking, listening, reading, writing
        sections = data.get("sections", [])
        for sec in sections:
            sec_title = format_text(sec.get("title", ""))
            body_parts.append(f'<div class="section-title">{sec_title}</div>')
            for item in sec.get("items", []):
                body_parts.append(
                    f'<div class="checklist-item"><span class="custom-cb"></span><span>{format_text(item)}</span></div>'
                )

    inner_content = "\n".join(body_parts)

    total_items = 0
    if "items" in data:
        total_items += len(data["items"])
    if "sections" in data:
        for sec in data["sections"]:
            total_items += len(sec.get("items", []))
            
    if total_items <= 7:
        spacing_class = "spacing-spacious"
    elif total_items <= 10:
        spacing_class = "spacing-normal"
    else:
        spacing_class = "spacing-compact"

    return f"""<div class="ie_fix">
<div class="content-container {spacing_class}">
{inner_content}
</div>
{badge_html}
</div>"""


def build_html(output_path: str = None) -> str:
    """Generate the complete self-contained French C2 HTML document."""
    if output_path is None:
        output_path = DEFAULT_OUTPUT_PATH

    print("Loading and base64-encoding fonts...")
    fonts_css = load_fonts_css()
    kerning_css = generate_kerning_css()

    print("Building HTML pages 1 to 71...")
    pages_html = []

    for p_num in range(1, 72):
        data = C2_PAGES_DATA[p_num]
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

    pages_joined = "\n".join(pages_html)

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<!-- French Learning Roadmap & Checklist -->
<meta name="description" content="French Learning Roadmap &amp; Checklist - French C2">
<title>French Learning Roadmap &amp; Checklist - French C2</title>
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
  border: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  display: block !important;
}}
.text_layer {{
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 902px !important;
  height: 1166px !important;
  overflow: hidden !important;
  z-index: 2 !important;
}}
.text_layer .ie_fix {{
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
}}
.text_layer span.a {{
  position: absolute !important;
  display: inline-block !important;
  white-space: pre !important;
  transform-origin: 0 0 !important;
}}

/* Clean Masking & Geometry */
.content-container {{
  position: absolute;
  top: 144px;
  left: 36px;
  width: 830px;
  min-height: 940px;
  background: #ffffff;
  box-sizing: border-box;
  padding: 16px 24px;
  z-index: 5;
}}

/* Safe Zones for Scribd Illustrations */
#page30 .content-container {{
  background: transparent !important;
  width: 440px !important;
  left: 55px !important;
  padding: 14px 18px;
}}
#page30 .checklist-item, #page30 .section-title, #page30 .page-intro, #page30 .page-title, #page30 .page-subtitle {{
  background: rgba(255, 255, 255, 0.94);
  padding: 4px 8px;
  border-radius: 4px;
}}

#page71 .content-container {{
  background: #ffffff !important;
  width: 480px !important;
  left: 45px !important;
  min-height: 940px;
  padding: 12px 16px;
}}
#page71 .checklist-item, #page71 .section-title, #page71 .page-intro, #page71 .page-title, #page71 .page-subtitle {{
  background: transparent;
  padding: 0;
  border-radius: 0;
}}
#page71 .readiness-box {{
  width: 450px;
  background: #f0fdf4 !important;
  border: 2px solid #22c55e;
  border-radius: 8px;
  padding: 14px 16px;
  margin-top: 16px;
}}

.content-container * {{
  white-space: normal;
  box-sizing: border-box;
}}
.page-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 28px;
  font-weight: bold;
  color: #1a1a1a;
  margin-bottom: 6px;
  line-height: 1.25;
}}
.page-subtitle {{
  font-family: "ff119", Arial, sans-serif;
  font-size: 17px;
  font-weight: bold;
  color: #1e1b4b;
  margin-bottom: 12px;
  line-height: 1.35;
}}
.page-intro {{
  font-family: "ff119", Arial, sans-serif;
  font-size: 15.5px;
  line-height: 1.55;
  color: #333333;
  margin-bottom: 22px;
}}
.section-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 20px;
  font-weight: bold;
  color: #1a1a1a;
  margin-top: 28px;
  margin-bottom: 14px;
  padding-bottom: 4px;
  border-bottom: 2px solid #eaeaea;
}}
.checklist-item {{
  display: flex;
  align-items: flex-start;
  margin-bottom: 18px;
  font-family: "ff119", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.55;
  color: #222221;
  gap: 14px;
}}
.custom-cb {{
  display: inline-block;
  width: 20px;
  height: 20px;
  min-width: 20px;
  border: 2.2px solid #1e1b4b;
  border-radius: 4px;
  background: #ffffff;
  margin-top: 2px;
}}
.green-check {{
  display: inline-block;
  width: 20px;
  height: 20px;
  min-width: 20px;
  line-height: 20px;
  text-align: center;
  border-radius: 50%;
  background: #74a866;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  margin-top: 2px;
}}
.outcome-check-item {{
  display: flex;
  align-items: flex-start;
  margin-bottom: 14px;
  font-family: "ff119", Arial, sans-serif;
  font-size: 15px;
  line-height: 1.45;
  color: #222221;
  gap: 12px;
}}
.footer-title {{
  font-family: "ff143", "Trebuchet MS", Arial, sans-serif;
  font-size: 18px;
  font-weight: bold;
  color: #1a1a1a;
  margin-top: 24px;
  margin-bottom: 14px;
  padding-bottom: 4px;
  border-bottom: 2px solid #eaeaea;
}}

/* Dynamic vertical spacing classes */
.spacing-spacious .checklist-item {{
  margin-bottom: 22px;
  font-size: 16.5px;
  line-height: 1.6;
}}
.spacing-spacious .section-title {{
  margin-top: 32px;
  margin-bottom: 16px;
  font-size: 21px;
}}
.spacing-spacious .page-intro {{
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 24px;
}}

.spacing-normal .checklist-item {{
  margin-bottom: 16px;
  font-size: 15.5px;
  line-height: 1.5;
}}
.spacing-normal .section-title {{
  margin-top: 24px;
  margin-bottom: 12px;
  font-size: 19.5px;
}}
.spacing-normal .page-intro {{
  font-size: 15px;
  line-height: 1.5;
  margin-bottom: 18px;
}}

.spacing-compact .checklist-item {{
  margin-bottom: 11px;
  font-size: 14px;
  line-height: 1.4;
}}
.spacing-compact .section-title {{
  margin-top: 16px;
  margin-bottom: 8px;
  font-size: 17.5px;
}}
.spacing-compact .page-intro {{
  font-size: 14px;
  line-height: 1.4;
  margin-bottom: 12px;
}}

.outcomes-table, .functions-table {{
  width: 100%;
  border-collapse: collapse;
  margin-top: 14px;
  margin-bottom: 18px;
  font-family: "ff119", Arial, sans-serif;
  font-size: 14px;
  line-height: 1.45;
}}
.outcomes-table th, .functions-table th {{
  background: #f1f5f9;
  color: #1e1b4b;
  font-weight: bold;
  text-align: left;
  padding: 10px 12px;
  border: 1px solid #cbd5e1;
  font-size: 14.5px;
}}
.outcomes-table td, .functions-table td {{
  padding: 9px 12px;
  border: 1px solid #cbd5e1;
  vertical-align: top;
  color: #334155;
}}
.outcomes-table tr:nth-child(even), .functions-table tr:nth-child(even) {{
  background: #f8fafc;
}}

.page-badge {{
  position: absolute !important;
  left: 811.6px !important;
  top: 1116px !important;
  width: 32px !important;
  height: 20px !important;
  font-family: "ff119", Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: bold !important;
  color: #444444 !important;
  text-align: right !important;
  z-index: 10 !important;
  line-height: 20px !important;
}}

{fonts_css}
{kerning_css}



/* Resource Card Styles */
.resource-card {{
  background: #ffffff !important;
  border: 1px solid #cbd5e1 !important;
  border-left: 5px solid #1e1b4b !important;
  border-radius: 8px !important;
  padding: 8px 12px !important;
  margin-bottom: 10px !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
}}
.resource-card-header {{
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 4px !important;
  padding-bottom: 3px !important;
  border-bottom: 1px solid #f1f5f9 !important;
}}
.resource-name {{
  font-size: 15px !important;
  font-weight: bold !important;
  color: #1e293b !important;
}}
.resource-badge {{
  background: #f1f5f9 !important;
  color: #1e1b4b !important;
  border: 1px solid #1e1b4b !important;
  padding: 2px 7px !important;
  border-radius: 12px !important;
  font-size: 10px !important;
  font-weight: bold !important;
}}
.resource-row {{
  font-size: 11.5px !important;
  line-height: 1.4 !important;
  color: #334155 !important;
  margin-bottom: 3px !important;
}}
.resource-label {{
  font-weight: bold !important;
  color: #0f172a !important;
}}
.resource-url {{
  color: #1e1b4b !important;
  font-family: monospace !important;
  font-size: 11px !important;
}}

</style>
</head>
<body>
{pages_joined}
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"French C2 HTML generated successfully: {output_path} ({size_mb:.2f} MB, 71 pages)")
    return output_path


if __name__ == "__main__":
    build_html()
