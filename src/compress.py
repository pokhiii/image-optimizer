# src/compress.py

import os
from PIL import Image

def compress_image(input_path, output_dir="compressed", quality=70, max_size=(1280, 1280)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, filename)

    with Image.open(input_path) as img:
        img.thumbnail(max_size, Image.LANCZOS)
        img.save(output_path, optimize=True, quality=quality)

    print(f"🗜️ Compressed & scaled: {filename} -> {output_path}")
