import os

DOWNLOADS_DIR = "downloads"
COMPRESSED_DIR = "compressed"

def get_file_sizes(directory):
    sizes = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            sizes[filename] = os.path.getsize(filepath)
    return sizes

def format_size(bytes_val):
    return f"{bytes_val / (1024 * 1024):.2f} MB"

original_sizes = get_file_sizes(DOWNLOADS_DIR)
compressed_sizes = get_file_sizes(COMPRESSED_DIR)

data = []
total_original = 0
total_compressed = 0

for filename, orig_size in original_sizes.items():
    comp_size = compressed_sizes.get(filename)
    if comp_size is None:
        continue
    saved = orig_size - comp_size
    data.append((filename, orig_size, comp_size, saved))
    total_original += orig_size
    total_compressed += comp_size

# Sort by saved bytes descending
data.sort(key=lambda x: x[3], reverse=True)

# Print the table
print(f"{'Filename':30} {'Original':>10} {'Compressed':>12} {'Saved':>10}")
print("-" * 66)
for filename, orig, comp, saved in data:
    print(f"{filename:30} {format_size(orig):>10} {format_size(comp):>12} {format_size(saved):>10}")

# Print totals
total_saved = total_original - total_compressed
print("-" * 66)
print(f"{'TOTAL':30} {format_size(total_original):>10} {format_size(total_compressed):>12} {format_size(total_saved):>10}")
