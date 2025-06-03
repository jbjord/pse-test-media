import os
import csv
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def process_csv(file_path, silent, max_threads):
    """Process the CSV file and call make_single_video.py for each filename using multiple threads."""
    try:
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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <csv_file_path> [--silent] [max_threads]")
    else:
        csv_file_path = sys.argv[1]
        silent_mode = '--silent' in sys.argv
        max_threads = int(sys.argv[sys.argv.index('--max_threads') + 1]) if '--max_threads' in sys.argv else 4
        process_csv(csv_file_path, silent_mode, max_threads)