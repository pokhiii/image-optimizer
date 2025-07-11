# src/image_utils.py
from PIL import Image
import os

def compress_image(path, max_size=(1280, 1280), quality=80):
    try:
        img = Image.open(path)
        img.thumbnail(max_size, Image.LANCZOS)

        # Convert RGBA to RGB to avoid PNG transparency issues
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(path, optimize=True, quality=quality)
        print(f"✅ Compressed: {os.path.basename(path)}")
    except Exception as e:
        print(f"❌ Failed to compress {path}: {e}")
