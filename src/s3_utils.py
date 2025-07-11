import boto3
import os

BUCKET_NAME = "aistudent.community"
s3 = boto3.client("s3")

def list_large_images(min_size_mb=5):
    paginator = s3.get_paginator('list_objects_v2')
    large_files = []
    for page in paginator.paginate(Bucket=BUCKET_NAME):
        for obj in page.get('Contents', []):
            key = obj['Key']
            size_mb = obj['Size'] / (1024 * 1024)
            if size_mb >= min_size_mb and key.lower().endswith(('.jpg', '.jpeg', '.png')):
                large_files.append((key, round(size_mb, 2)))
    return large_files

def download_file(key, dest_folder="downloads"):
    os.makedirs(dest_folder, exist_ok=True)
    filename = os.path.join(dest_folder, os.path.basename(key))
    s3.download_file(BUCKET_NAME, key, filename)
    return filename
