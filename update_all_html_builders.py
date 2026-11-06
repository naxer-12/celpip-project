#!/usr/bin/env python3
"""
update_all_html_builders.py - Update all 5 level HTML builders with .resource-card styling and rendering
"""

import os
import re

BUILDERS = [
    ("French_A2/build_a2_html.py", "#2572be"),
    ("French_B1/build_b1_html.py", "#6b46c1"),
    ("French_B2/build_b2_html.py", "#9f1239"),
    ("French_C1/build_c1_html.py", "#047857"),
    ("French_C2/build_c2_html.py", "#1e1b4b"),
]

RESOURCE_HANDLER = """
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
                f'<div class="resource-card">\\n'
                f'  <div class="resource-card-header">\\n'
                f'    <span class="resource-name">{name}</span>\\n'
                f'    <span class="resource-badge">{badge}</span>\\n'
                f'  </div>\\n'
                f'  <div class="resource-row"><span class="resource-label">Platform / URL:</span> <span class="resource-url">{url}</span></div>\\n'
                f'  <div class="resource-row"><span class="resource-label">Content:</span> {what}</div>\\n'
                f'  <div class="resource-row"><span class="resource-label">Key Features:</span> {features}</div>\\n'
                f'  <div class="resource-row"><span class="resource-label">Focus:</span> {focus}</div>\\n'
                f'  <div class="resource-row"><span class="resource-label">Study Routine:</span> {tips}</div>\\n'
                f'  <div class="checklist-item" style="margin-top:6px; margin-bottom:0;"><span class="custom-cb"></span><span>Mark as active weekly study resource</span></div>\\n'
                f'</div>'
            )
"""

def get_css(accent):
    return f"""
/* Resource Card Styles */
.resource-card {{
  background: #ffffff !important;
  border: 1px solid #cbd5e1 !important;
  border-left: 5px solid {accent} !important;
  border-radius: 8px !important;
  padding: 9px 13px !important;
  margin-bottom: 11px !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
}}
.resource-card-header {{
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 5px !important;
  padding-bottom: 4px !important;
  border-bottom: 1px solid #f1f5f9 !important;
}}
.resource-name {{
  font-size: 15.5px !important;
  font-weight: bold !important;
  color: #1e293b !important;
}}
.resource-badge {{
  background: #f1f5f9 !important;
  color: {accent} !important;
  border: 1px solid {accent} !important;
  padding: 2px 8px !important;
  border-radius: 12px !important;
  font-size: 10.5px !important;
  font-weight: bold !important;
}}
.resource-row {{
  font-size: 12px !important;
  line-height: 1.42 !important;
  color: #334155 !important;
  margin-bottom: 3px !important;
}}
.resource-label {{
  font-weight: bold !important;
  color: #0f172a !important;
}}
.resource-url {{
  color: {accent} !important;
  font-family: monospace !important;
  font-size: 11.5px !important;
}}
"""

def update_builder(filepath, accent):
    print(f"Updating {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if resource handler already exists
    if 'elif p_type == "resources":' not in content:
        # Insert before "elif p_type == "audit":"
        target = 'elif p_type == "audit":'
        if target in content:
            content = content.replace(target, RESOURCE_HANDLER + "\n    " + target)
        else:
            print(f"WARNING: Could not find target in {filepath}")
            
    # Check if resource CSS already exists
    if '.resource-card {' not in content:
        css = get_css(accent)
        target_css = '</style>'
        content = content.replace(target_css, css + "\n" + target_css)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} successfully.")

def main():
    for filepath, accent in BUILDERS:
        update_builder(filepath, accent)

if __name__ == "__main__":
    main()
