import os
import shutil
import argparse
from utils.json_utils import merge_with_config

def cleanup_directory(json_file_path, silent=False):
    # Load JSON
    data = merge_with_config(json_file_path)
    
    # Get directory to delete
    json_dir = os.path.dirname(json_file_path)
    json_filename = os.path.splitext(os.path.basename(json_file_path))[0]
    directory_to_delete = data.get('save_directory', f"{json_filename}_src")
    full_directory_path = os.path.join(json_dir, directory_to_delete)
    
    # Delete directory and all contents
    if os.path.exists(full_directory_path):
        shutil.rmtree(full_directory_path)
        if not silent:
            print(f"Deleted directory: {full_directory_path}")
    else:
        if not silent:
            print(f"Directory does not exist: {full_directory_path}")

def main():
    parser = argparse.ArgumentParser(description="Cleanup script to delete directories specified in a JSON file.")
    parser.add_argument('json_file_path', metavar='JSON_FILE', type=str, nargs='?',
                        help='Path to the JSON file that specifies the directory to delete.')
    parser.add_argument('--silent', action='store_true', default=False,
                        help='Run the script in silent mode without printing any output.')

    # Parse arguments
    args = parser.parse_args()

    # Check if JSON file path is provided
    if args.json_file_path:
        cleanup_directory(args.json_file_path, silent=args.silent)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()