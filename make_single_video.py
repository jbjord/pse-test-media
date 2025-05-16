import subprocess
import argparse
import time


def main():
    '''Runs all scripts necessary to create a single video from a JSON file and cleans up interim files'''
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Run scripts for creating a video sequentially.')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('--silent', action='store_true', help='Suppress output')
    parser.add_argument('--precedence', type=str, choices=['config', 'custom'], default='custom',
                        help='Specify which JSON settings take precedence (default = custom)')
    args = parser.parse_args()
    
    # Record the total start time
    total_start_time = time.time()

    try:
        # Run generate_frames.py
        if (not args.silent):
            print(" #1 Running generate_frames.py...")
        start_time = time.time()
        subprocess.run(
            ['python', 'generate_frames.py', args.json_file],
            check=True,
            stdout=subprocess.DEVNULL if args.silent else None,
            stderr=subprocess.DEVNULL if args.silent else None
        )
        end_time = time.time()
        if (not args.silent):
            print(f"   generate_frames.py took {end_time - start_time:.2f} seconds")

        # Run generate_video.py
        if (not args.silent):
            print(" #2 Running generate_video.py...")
        start_time = time.time()
        subprocess.run(
            ['python', 'generate_video.py', args.json_file],
            check=True,
            stdout=subprocess.DEVNULL if args.silent else None,
            stderr=subprocess.DEVNULL if args.silent else None
        )
        end_time = time.time()
        if (not args.silent):
            print(f"   generate_video.py took {end_time - start_time:.2f} seconds")

        # Run clean_up.py
        if (not args.silent):
            print(" #3 Running clean_up.py...")
        start_time = time.time()
        subprocess.run(
            ['python', 'clean_up.py', args.json_file],
            check=True,
            stdout=subprocess.DEVNULL if args.silent else None,
            stderr=subprocess.DEVNULL if args.silent else None
        )
        end_time = time.time()
        if (not args.silent):
            print(f"   clean_up.py took {end_time - start_time:.2f} seconds")

        # Record the total end time
        total_end_time = time.time()
        if (not args.silent):
            print(f" Done. Time = {total_end_time - total_start_time:.2f} seconds.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()