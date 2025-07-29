import json
import os

def remove_keys_from_obj(obj):
    """Recursively remove specified keys and empty 'invalid_tool_calls' or empty 'additional_kwargs' from a JSON object."""
    if isinstance(obj, dict):
        # Use a list of keys to remove to avoid modifying the dictionary while iterating
        keys_to_remove = [key for key in obj if key in ['id', 'index', 'tool_call_id', 'response_metadata', 'usage_metadata', 'example', 'artifact']]
        if 'invalid_tool_calls' in obj and isinstance(obj['invalid_tool_calls'], list) and not obj['invalid_tool_calls']:
            keys_to_remove.append('invalid_tool_calls')
        if 'additional_kwargs' in obj and isinstance(obj['additional_kwargs'], dict) and not obj['additional_kwargs']:
            keys_to_remove.append('additional_kwargs')
        if 'tool_calls' in obj and isinstance(obj['tool_calls'], list) and not obj['tool_calls']:
            keys_to_remove.append('tool_calls')
        if 'args' in obj and isinstance(obj['args'], dict) and not obj['args']:
            keys_to_remove.append('args')

        for key in keys_to_remove:
            del obj[key]
        # Recurse into the values
        for key in obj:
            obj[key] = remove_keys_from_obj(obj[key])
    elif isinstance(obj, list):
        # Recurse into list elements
        return [remove_keys_from_obj(item) for item in obj]
    return obj

def process_json_file(file_path):
    """Read a JSON file, remove specified keys, and write it back."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cleaned_data = remove_keys_from_obj(data)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, indent=4)
            
        print(f"Successfully processed {file_path}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_to_process = '/workspaces/Implementierung/runs/o4-mini/3-2/messages-clean.json'
    process_json_file(file_to_process)
