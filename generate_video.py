import cv2
import json
import os
import csv

def read_csv(file_path):
    csv_dir = os.path.dirname(file_path)
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [os.path.join(csv_dir, row['image_path']) for row in reader]

def generate_video(json_file):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Get JSON file's basename
    basename = os.path.basename(json_file).split('.')[0]
    
    # Set default CSV location if not specified in the JSON
    csv_path = os.path.join(os.path.dirname(json_file), f"{basename}_src/framelist.csv")
    
    # Read the CSV file containing frame paths
    frame_paths = read_csv(csv_path)
    
    # Print the read frame paths for debugging
    print("Read frame paths:")
    for frame_path in frame_paths:
        print(frame_path)
    
    # Extract video properties from JSON
    framerate = data.get('framerate', 30)
    codec = data.get('codec', 'ffv1')
    video_extension = data.get('video_extension', 'avi')
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*codec)
    output_video = os.path.join(os.path.dirname(json_file), f"{basename}.{video_extension}")
    
    # Print the first frame path for debugging
    first_frame_path = frame_paths[0]
    print(f"Reading first frame from: {first_frame_path}")

    # Read the first frame
    first_frame = cv2.imread(first_frame_path)
    if first_frame is None:
        raise FileNotFoundError(f"Cannot read the first frame from path: {first_frame_path}")
    
    height, width, _ = first_frame.shape
    video_writer = cv2.VideoWriter(output_video, fourcc, framerate, (width, height))
    
    # Add each frame to the video writer
    for frame_path in frame_paths:
        frame = cv2.imread(frame_path)
        if frame is None:
            print(f"Warning: Cannot read frame from path: {frame_path}")
            continue
        video_writer.write(frame)
    
    # Release the video writer
    video_writer.release()
    print(f"Video saved to {output_video}")

# Command line execution
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_video.py <path_to_json>")
    else:
        generate_video(sys.argv[1])
