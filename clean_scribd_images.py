#!/usr/bin/env python3
"""
clean_scribd_images.py - Clean all background images in scribd_raw/images/

1. On 1.jpg (cover template):
   - Erase the top white tab and 'The Language Network' logo by filling
     (350, 0, 555, 95) with the matching header sky-blue color (117, 203, 230).
2. On 2.jpg through 71.jpg:
   - Erase 'The Language Network' logo by filling (350, 35, 550, 140) with pure white #FFFFFF.
3. On pages 31 to 42, 44 to 52, and 53 to 67:
   - Erase any background table lines and website screenshots by filling
     the body rectangle (50, 150, 854, 1060) with pure white #FFFFFF,
     preserving the bottom-right page badge tab (750, 1070, 904, 1169).
"""

import os
from PIL import Image, ImageDraw

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scribd_raw", "images")

def clean_all():
    print(f"Cleaning background images in {IMAGES_DIR}...")
    
    # 1. Clean 1.jpg
    p1_path = os.path.join(IMAGES_DIR, "1.jpg")
    if os.path.exists(p1_path):
        im1 = Image.open(p1_path).convert("RGB")
        draw1 = ImageDraw.Draw(im1)
        # Sample header color at x=200, y=30
        header_color = im1.getpixel((200, 30))
        draw1.rectangle((350, 0, 555, 95), fill=header_color)
        im1.save(p1_path, quality=95)
        print("Cleaned 1.jpg")

    # 2. Clean 2.jpg to 71.jpg
    for p in range(2, 72):
        img_path = os.path.join(IMAGES_DIR, f"{p}.jpg")
        if not os.path.exists(img_path):
            continue
        im = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(im)
        
        # Erase top logo
        draw.rectangle((350, 35, 550, 140), fill="#FFFFFF")
        
        # Erase ghost tables (31-42, 44-52) and old screenshots (53-67)
        if (31 <= p <= 42) or (44 <= p <= 52) or (53 <= p <= 67):
            draw.rectangle((50, 150, 854, 1060), fill="#FFFFFF")
            
        im.save(img_path, quality=95)
        
    print("Cleaned all images 2.jpg through 71.jpg successfully.")

if __name__ == "__main__":
    clean_all()
