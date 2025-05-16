import json
import os

CONFIG_JSON_PATH = 'video_config.json'

def load_json(file_path):
    '''Load JSON data from a file.'''
    with open(file_path, 'r') as file:
        return json.load(file)


def merge_json(config_json, custom_json, precedence):
    '''Merge two JSON objects based on precedence.'''
    if precedence == 'custom':
        merged = {**config_json, **custom_json}
    else:
        merged = {**custom_json, **config_json}
    return merged


def merge_with_config(custom_json_path, precedence='custom'):
    '''Merge custom JSON with CONFIG_JSON_PATH if it exists'''
    custom_json = load_json(custom_json_path)

    # Check for the existence of the config JSON file
    if os.path.exists(CONFIG_JSON_PATH):
        config_json = load_json(CONFIG_JSON_PATH)
        # Merge JSON files based on precedence
        merged_json = merge_json(config_json, custom_json, precedence)
    else:
        print(f"Default JSON file '{CONFIG_JSON_PATH}' not found. Using only the custom JSON file.")
        merged_json = custom_json
    
    return merged_json