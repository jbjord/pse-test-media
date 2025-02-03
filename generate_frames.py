import csv
import numpy as np
from PIL import Image
import os
import json
import argparse

def recolor_image(png_path, r, g, b, a):
    with Image.open(png_path) as img:
        img = img.convert('RGBA')
        data = np.array(img)
        # Identify opaque pixels
        mask = data[:, :, 3] != 0
        # Recolor pixels
        data[mask] = [r, g, b, a]
        return Image.fromarray(data)


def merge_images(images, bg_color=None):
    if not images:
        return None
    merged = images[0].copy()
    for img in images[1:]:
        merged = Image.alpha_composite(merged, img)

    if bg_color is not None:
        # Create a background image with the specified background color
        bg_img = Image.new('RGBA', merged.size, bg_color)
        merged = Image.alpha_composite(bg_img, merged)

    return merged


def generate_frames(json_data, json_dir):
    pattern_list = json_data['pattern']
    unique_images = {}
    new_csv_data = []
    max_rows = 0

    # Determine the save directory
    save_dir = json_data.get('save_directory', os.path.join(json_dir, os.path.splitext(os.path.basename(json_path))[0] + '_src'))
    os.makedirs(save_dir, exist_ok=True)

    # Determine the background color
    bg_color_str = json_data.get('bgcolor')
    bg_color = None
    if bg_color_str:
        bg_color = tuple(map(int, bg_color_str.strip('()').split(',')))

    # Find the length of the longest CSV
    for pattern in pattern_list:
        temporal_path = os.path.join(json_dir, pattern['temporal_color'])
        with open(temporal_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            max_rows = max(max_rows, len(rows))

    # Process each row
    for row_idx in range(max_rows):
        recolored_images = []

        for pattern in pattern_list:
            spatial_path = os.path.join(json_dir, pattern['spatial'])
            temporal_path = os.path.join(json_dir, pattern['temporal_color'])

            with open(temporal_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                if row_idx < len(rows):
                    row = rows[row_idx]
                    r, g, b, a = int(row['r']), int(row['g']), int(row['b']), int(row['a'])
                    recolored_image = recolor_image(spatial_path, r, g, b, a)
                    recolored_images.append(recolored_image)

        merged_image = merge_images(recolored_images, bg_color)

        if merged_image is not None:
            merged_image_hash = hash(merged_image.tobytes())
            if merged_image_hash not in unique_images:
                unique_images[merged_image_hash] = merged_image

            # Determine the relative path from the CSV directory
            relative_image_path = os.path.relpath(os.path.join(save_dir, f"merged_{merged_image_hash}.png"), os.path.dirname(os.path.join(save_dir, 'framelist.csv')))
            unique_image_path = os.path.join(save_dir, f"merged_{merged_image_hash}.png")
            if not os.path.exists(unique_image_path):
                unique_images[merged_image_hash].save(unique_image_path)

            new_csv_data.append({
                'frame': row_idx,
                'image_path': relative_image_path
            })
            #print(f"Row {row_idx}: Merged image saved as {relative_image_path}")

    new_csv_path = os.path.join(save_dir, 'framelist.csv')
    with open(new_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['frame', 'image_path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in new_csv_data:
            writer.writerow(data)

# Command line execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate frames from JSON input.')
    parser.add_argument('json_path', type=str, help='Path to the JSON file.')

    args = parser.parse_args()
    json_path = args.json_path
    json_dir = os.path.dirname(os.path.abspath(json_path))

    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    generate_frames(json_data, json_dir)
