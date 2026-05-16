import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import config

def _ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_poster(title, caption, index):
    output_dir = os.path.join(config.BASE_DIR, "output", "images")
    _ensure_dir(output_dir)
    output_path = os.path.join(output_dir, f"post_{index}.jpg")
    
    print(f"🎨 Generating poster for post {index}...")
    
    # 1. Load Background or Create Default Dark Background
    bg_path = os.path.join(config.BASE_DIR, "assets", "background.jpg")
    try:
        if os.path.exists(bg_path) and os.path.getsize(bg_path) > 0:
            img = Image.open(bg_path).convert("RGB")
            img = img.resize((1080, 1080)) # Standard Instagram size
        else:
            raise ValueError("Empty background file")
    except Exception:
        # Fallback if background.jpg is empty/missing
        img = Image.new("RGB", (1080, 1080), color="#1a1a2e")
        
    draw = ImageDraw.Draw(img)
    
    # 2. Load Font or Default
    font_path = os.path.join(config.BASE_DIR, "assets", "font.ttf")
    try:
        if os.path.exists(font_path) and os.path.getsize(font_path) > 0:
            title_font = ImageFont.truetype(font_path, 50)
            caption_font = ImageFont.truetype(font_path, 30)
        else:
            raise ValueError("Empty font file")
    except Exception:
        # Fallback if font.ttf is empty/missing
        title_font = ImageFont.load_default()
        caption_font = ImageFont.load_default()
        
    # 3. Text Wrapping
    preview_caption = caption[:250] + "..." if len(caption) > 250 else caption
    wrapped_title = textwrap.fill(title, width=40)
    wrapped_caption = textwrap.fill(preview_caption, width=50)
    
    # 4. Draw Text
    draw.text((80, 150), wrapped_title, fill="#00e5ff", font=title_font)
    draw.text((80, 350), wrapped_caption, fill="#ffffff", font=caption_font)
    
    # 5. Export
    try:
        img.save(output_path, "JPEG")
        return output_path
    except Exception as e:
        print(f"❌ Failed to save poster image: {e}")
        return None
