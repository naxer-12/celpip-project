import os
from PIL import Image, ImageDraw, ImageFont

def generate_b2_cover(src_path=None, dst_path=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if src_path is None:
        src_path = os.path.join(base_dir, "scribd_raw", "images", "1.jpg")
    if dst_path is None:
        dst_path = os.path.join(base_dir, "scribd_raw", "images", "1_b2.jpg")
        
    im = Image.open(src_path).convert("RGB")
    draw = ImageDraw.Draw(im)
    
    # Deep ruby crimson background: #9f1239
    pill_box = (365, 324, 538, 376)
    draw.rounded_rectangle(pill_box, radius=10, fill="#9f1239")
    
    font = None
    for font_path in [
        "/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf",
        "/System/Library/Fonts/Supplemental/Verdana Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf"
    ]:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, 34)
                break
            except Exception:
                continue
    if font is None:
        font = ImageFont.load_default()
        
    text = "French B2"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    text_x = pill_box[0] + (pill_box[2] - pill_box[0] - text_w) / 2 - bbox[0]
    text_y = pill_box[1] + (pill_box[3] - pill_box[1] - text_h) / 2 - bbox[1]
    
    draw.text((text_x, text_y), text, fill="#ffffff", font=font)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    im.save(dst_path, quality=95)
    print("Generated:", dst_path)
    return dst_path

if __name__ == "__main__":
    generate_b2_cover()
