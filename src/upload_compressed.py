import os
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "aistudent.community"
COMPRESSED_FOLDER = "compressed"

s3 = boto3.client("s3")

def upload_file(filepath, key):
    try:
        with open(filepath, "rb") as f:
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=key,
                Body=f,
                ContentType=detect_content_type(key),
                CacheControl="public, max-age=2592000, immutable",
                ServerSideEncryption="AES256",
            )
        print(f"✅ Uploaded: {key}")
    except ClientError as e:
        print(f"❌ Failed: {key} - {e}")

def detect_content_type(filename):
    if filename.lower().endswith(".png"):
        return "image/png"
    if filename.lower().endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    return "binary/octet-stream"

def main():
    files = [f for f in os.listdir(COMPRESSED_FOLDER)
             if os.path.isfile(os.path.join(COMPRESSED_FOLDER, f))
             and not f.startswith(".")  # skip .gitkeep and dotfiles
             and f.lower().endswith((".png", ".jpg", ".jpeg"))]

    total = len(files)
    print(f"🚀 Starting upload of {total} compressed images...\n")

    for idx, filename in enumerate(files, start=1):
        filepath = os.path.join(COMPRESSED_FOLDER, filename)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"[{idx}/{total}] Uploading {filename} ({size_mb:.2f} MB)")
        upload_file(filepath, key=filename)

    print(f"\n✅ Upload complete: {total} files uploaded.")

# def main():
#     filename = "...." // enter file name
#     filepath = os.path.join(COMPRESSED_FOLDER, filename)
#     if os.path.isfile(filepath):
#         upload_file(filepath, key=filename)
#     else:
#         print(f"❌ File not found: {filepath}")

if __name__ == "__main__":
    main()
