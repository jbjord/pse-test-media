import sys
import os
import cv2
import numpy as np

def count_opaque_pixels(image_path):
    # Load the image with transparency (alpha channel)
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if image is None:
        raise ValueError(f"Could not open or find the image {image_path}")

    # Check if the image has an alpha channel
    if image.shape[2] != 4:
        raise ValueError("Image does not have an alpha channel")

    # Extract the alpha channel
    alpha_channel = image[:, :, 3]
    
    # Convert to an integer array
    opaque_pixels = cv2.countNonZero((alpha_channel == 255).astype(np.uint8))
    total_pixels = image.shape[0] * image.shape[1]
    
    return opaque_pixels, total_pixels

def process_folder(folder_path):
    data = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                image_path = os.path.join(root, file)
                try:
                    opaque_pixels, total_pixels = count_opaque_pixels(image_path)
                    percentage_opaque = (opaque_pixels / total_pixels) * 100
                    data.append((file, total_pixels, opaque_pixels, percentage_opaque))
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_png_or_folder>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    if os.path.isdir(path):
        data = process_folder(path)
        print(f"{'File Name':<30} {'Total Pixels':<15} {'Opaque Pixels':<15} {'Opaque Percent':<15}")
        for row in data:
            print(f"{row[0]:<30} {row[1]:<15} {row[2]:<15} {row[3]:<15.2f}")
    elif os.path.isfile(path) and path.lower().endswith('.png'):
        opaque_pixels, total_pixels = count_opaque_pixels(path)
        percentage_opaque = (opaque_pixels / total_pixels) * 100
        print(f"Total number of pixels: {total_pixels}")
        print(f"Number of opaque pixels: {opaque_pixels}")
        print(f"Percentage of opaque pixels: {percentage_opaque:.2f}%")
    else:
        print(f"Invalid path: {path}")
        sys.exit(1)

if __name__ == "__main__":
    main()