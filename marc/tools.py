MARC_WORKSPACE_PATH = "../marc_workspace"

# Tools
def generate_puml_diagram(puml: str):
    """Generate PlantUML Diagram based on a given puml text"""
    return "Successfully generated the desired diagram!" 


def write_file(text: str, filepath: str):
    """Write a text to a file with a specific format"""
    try:
        with open(f"{MARC_WORKSPACE_PATH}/{filepath}", "w") as file:
            file.write(text)
            return "Successfully wrote file"
    except Exception as e:
        return f"Error writing file {filepath}: {e}"

def read_file(filepath: str):
    """Read a text from a file with a specific format"""
    try:
        with open(f"{MARC_WORKSPACE_PATH}/{filepath}", "r") as file:
            text = file.read()
            return text
    except Exception as e:
        return f"Error reading file {filepath}: {e}"

def discover_filesystem():
    """Return a complete representation of the filesystem with all files, directories and all recursive subdirectories, execpt directories and file that start with '.'."""
    import os

    def get_filesystem_structure(path):
        structure = {}
        for item in os.listdir(path):
            if item.startswith('.'):
                continue
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                structure[item] = get_filesystem_structure(item_path)
            else:
                structure[item] = None
        return structure

    filesystem_structure = get_filesystem_structure(MARC_WORKSPACE_PATH)
    return filesystem_structure
