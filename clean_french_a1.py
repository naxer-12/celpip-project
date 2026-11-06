#!/usr/bin/env python3
"""
clean_french_a1.py - Remove 'The Language Network' logo from French A1 HTML and recompile PDF
"""

import os
import re
import io
import base64
from PIL import Image, ImageDraw

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "French_A1", "French_Learning_Roadmap_Checklist_French_A1.html")
PDF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "French_A1", "French_Learning_Roadmap_Checklist_French_A1.pdf")

def clean_a1():
    print(f"Reading {HTML_PATH}...")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Pattern for absimg
    pattern = re.compile(r'(<img[^>]*class="absimg"[^>]*src="data:image/jpeg;base64,)([^"]+)(")')
    
    matches = list(pattern.finditer(html_content))
    print(f"Found {len(matches)} images in A1 HTML.")
    
    # Process from last to first so indices don't shift
    modified_html = html_content
    for idx in range(len(matches) - 1, -1, -1):
        m = matches[idx]
        p_num = idx + 1
        b64_str = m.group(2)
        img_bytes = base64.b64decode(b64_str)
        im = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        draw = ImageDraw.Draw(im)
        
        if p_num == 1:
            header_color = im.getpixel((200, 30))
            draw.rectangle((350, 0, 555, 95), fill=header_color)
        else:
            draw.rectangle((350, 35, 550, 140), fill="#FFFFFF")
            
        out_buf = io.BytesIO()
        im.save(out_buf, format="JPEG", quality=95)
        new_b64 = base64.b64encode(out_buf.getvalue()).decode("ascii")
        
        start = m.start(2)
        end = m.end(2)
        modified_html = modified_html[:start] + new_b64 + modified_html[end:]
        
    print(f"Writing updated A1 HTML to {HTML_PATH}...")
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(modified_html)
        
    print(f"Compiling clean French A1 PDF...")
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = (
        f'"{chrome_bin}" --headless --disable-gpu --no-pdf-header-footer '
        f'--print-to-pdf="{PDF_PATH}" "file://{HTML_PATH}"'
    )
    res = os.system(cmd)
    if res == 0:
        print(f"Successfully compiled: {PDF_PATH}")
    else:
        print(f"Chrome exit code: {res}")

if __name__ == "__main__":
    clean_a1()
