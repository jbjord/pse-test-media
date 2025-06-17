import os
import csv
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def process_csv(path, silent, max_threads):
    """Process the CSV file and call make_single_video.py for each filename using multiple threads."""
    try:
        # Determine if the path is a directory or a file
        if os.path.isdir(path):
            # If it's a directory, construct the CSV file path using the directory name
            directory_name = os.path.basename(path)
            file_path = os.path.join(path, f"{directory_name}.csv")
        else:
            # If it's a file, use the provided path directly
            file_path = path

        # Get the directory of the CSV file
        csv_directory = os.path.dirname(file_path)

        with open(file_path, mode='r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            filenames = [row['filename'] for row in csvreader if 'filename' in row]

        if not filenames:
            print("The CSV does not contain a 'filename' column.")
            return

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [
                executor.submit(call_make_single_video, os.path.join(csv_directory, f"{filename}.json"), silent)
                for filename in filenames
            ]
            for future in futures:
                future.result()  # Wait for all threads to complete

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def call_make_single_video(json_file, silent):
    """Call the make_single_video.py script with the given JSON file."""
    try:
        command = ['python', 'make_single_video.py', json_file]
        if silent:
            command.append('--silent')
        subprocess.run(command, check=True)
        print(f"Processed {json_file} with {'--silent' if silent else 'no'} silent mode")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while processing {json_file}: {e}")


def print_help():
    """Print help information."""
    print("""
**Usage:**
  python make_videos.py <csv_file_path_or_directory> [--silent] [--max_threads <number>]

**Options:**
  -h, --help            Show this help message and exit.
  --silent              Run the script in silent mode.
  --max_threads <number> Specify the maximum number of threads to use. Default is 4.

**Examples:**
  python make_videos.py /path/to/directory/csvfile.csv
  python make_videos.py /path/to/directory --silent
  python make_videos.py /path/to/directory --max_threads 8

**Description:**
  This multi-thread script processes a CSV file and calls make_single_video.py for each JSON file listed in the CSV.
  If a directory path is provided, it assumes the CSV file is named after the directory.
    """)

if __name__ == '__main__':
    if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
        print_help()
    else:
        path = sys.argv[1]
        silent_mode = '--silent' in sys.argv
        max_threads = int(sys.argv[sys.argv.index('--max_threads') + 1]) if '--max_threads' in sys.argv else 4
        process_csv(path, silent_mode, max_threads)
