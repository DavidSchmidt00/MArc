MARC_WORKSPACE_PATH = "marc_workspace"

# Tools
def generate_puml_diagram(puml: str):
    """Generate PlantUML Diagram based on a given puml text"""
    return "Successfully generated the desired diagram!" 


def write_file(text: str, filepath: str):
    f"""Write a text to a file with a specific format
    
    Args:
        text (str): The text to write to the file.
        filepath (str): The path where the file should be written.`.
    """
    try:
        with open(f"{MARC_WORKSPACE_PATH}/{filepath}", "w") as file:
            file.write(text)
            return "Successfully wrote file"
    except Exception as e:
        return f"Error writing file {filepath}: {e}"

def read_file(filepath: str):
    f"""Read a text from a file with a specific format
    
    Args:
        filepath (str): The path to the file to read.`.
    """
    try:
        with open(f"{MARC_WORKSPACE_PATH}/{filepath}", "r") as file:
            text = file.read()
            return text
    except Exception as e:
        return f"Error reading file {filepath}: {e}" 

def discover_filesystem():
    """Return a complete textual representation of the filesystem with all files, directories and all recursive subdirectories, even if they are empty."""
    import os

    def list_files(startpath):
        result = []
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            result.append(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                result.append(f"{subindent}{f}")
        return "\n".join(result)

    return list_files(MARC_WORKSPACE_PATH)
