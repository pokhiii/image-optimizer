import os
from compress import compress_image

DOWNLOAD_DIR = "downloads"

for filename in os.listdir(DOWNLOAD_DIR):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(DOWNLOAD_DIR, filename)
        compress_image(input_path)
