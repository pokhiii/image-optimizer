from s3_utils import list_large_images, download_file

def main():
    print("🔍 Listing large images (>5MB)...")
    files = list_large_images()
    for key, size in files:
        print(f"📥 Downloading: {key} ({size} MB)")
        download_file(key)
    print("✅ Done downloading.")

if __name__ == "__main__":
    main()
