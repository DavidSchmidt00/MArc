import os
import shutil

from langchain_core.tools import tool

from typing import Annotated

from plantweb.render import render

WORKSPACE = "/workspaces/Implementierung/workspace/"

@tool(description="Write content to a file at the specified path. If the file does not exist, it will be created. If the parent directories do not exist, they will be created as well. If the file already exists, it will be overwritten.")
def write_file(file_path: Annotated[str, "Path of the file that should be written"], content: Annotated[str, "Content to write into the file"]) -> Annotated[dict, "Status of the write operation (contains 'status' and 'message' or 'error_message')"]:
  try:
    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(WORKSPACE+file_path), exist_ok=True)
    with open(WORKSPACE+file_path, 'w', encoding='utf-8') as f:
      f.write(content)
    return {
        'status': 'success',
        'message': f'File successfully written to {file_path}.'
    }
  except IOError as e:
    return {
        'status': 'error',
        'error_message': f'Error writing file {file_path}: {e}'
    }
  except Exception as e:
    return {
        'status': 'error',
        'error_message': f'Unexpected error writing file {file_path}: {e}'
    }

@tool(description="Read the content of a file at the specified path.")
def read_file(file_path: Annotated[str, "Path of the file that should be read"]) -> Annotated[dict, "Status of the read operation (contains 'status' and 'content' or 'error_message')"]:
  try:
    with open(WORKSPACE+file_path, 'r', encoding='utf-8') as f:
      content = f.read()
    return {
        'status': 'success',
        'content': content
    }
  except FileNotFoundError as e:
    return {
        'status': 'error',
        'error_message': f'The file at path {file_path} was not found: {e}'
    }
  except IOError as e:
    return {
        'status': 'error',
        'error_message': f'Error reading file {file_path}: {e}'
    }
  except Exception as e:
    return {
        'status': 'error',
        'error_message': f'Unexpected error reading file {file_path}: {e}'
    }

@tool(description="Initialize arc42 documentation, creating the necessary directory structure and copying the template files. This should be done only once per project. Existing files will not be overwritten.")
def initialize_arc42_documentation() -> Annotated[dict, "Status of the initialization operation (contains 'status' and 'message' or 'error_message')"]:
  try:
    template_path = '/workspaces/Implementierung/template/'
    if not os.path.exists(template_path):
      return {
          'status': 'error',
          'error_message': f'The arc42 template directory {template_path} does not exist.'
      }
    
    # Create target directory if it doesn't exist
    path = f"architectures/"
    target_path = WORKSPACE+path
    os.makedirs(target_path, exist_ok=True)

    # Copy directory structure recursively, skipping existing files
    for item in os.listdir(template_path):
      s = os.path.join(template_path, item)
      d = os.path.join(target_path, item)
      if os.path.exists(d):
        continue  # Skip if destination already exists
      if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
      else:
        shutil.copy2(s, d)

    return {
        'status': 'success',
        'message': f'arc42 documentation successfully initialized under {path}.'
    }
  except OSError as e:
    return {
        'status': 'error',
        'error_message': f'File system error initializing arc42 documentation: {e}'
    }
  except shutil.Error as e:
    return {
        'status': 'error',
        'error_message': f'Copy error initializing arc42 documentation: {e}'
    }
  except Exception as e:
    return {
        'status': 'error',
        'error_message': f'Unexpected error initializing arc42 documentation: {e}'
    }

@tool(description="List all files and directories in the workspace and return the directory structure as text.")
def discover_filesystem() -> Annotated[dict, "Status of the discovery operation (contains 'status' and 'structure' or 'error_message')"]:
  try:
    if not os.path.isdir(WORKSPACE):
      return {
          'status': 'error',
          'error_message': f'The workspace directory {WORKSPACE} is not a directory or does not exist.'
      }

    tree_string = ""
    for root, dirs, files in os.walk(WORKSPACE):
      level = root.replace(WORKSPACE, '').count(os.sep)
      indent = ' ' * 4 * (level)
      tree_string += f'{indent}{os.path.basename(root)}/\n'
      sub_indent = ' ' * 4 * (level + 1)
      for f in files:
        tree_string += f'{sub_indent}{f}\n'

    return {
        'status': 'success',
        'structure': tree_string
    }
  except OSError as e:
    return {
        'status': 'error',
        'error_message': f'File system error discovering workspace: {e}'
    }
  except Exception as e:
    return {
        'status': 'error',
        'error_message': f'Unexpected error discovering workspace: {e}'
    }

@tool(description="Render PlantUML content to SVG format and save both the PlantUML source and the rendered SVG.")
def render_plantuml_diagram(filename: Annotated[str, "Just the filename (No path!) for the diagram, without extension"], content: Annotated[str, "PlantUML content to render"]) -> Annotated[dict, "Status of the rendering operation (contains 'status' or 'error_message')"]:
  try:
    # Define paths for .puml and .svg files
    puml_path = f"architectures/diagrams/{filename}.puml"
    svg_path = f"architectures/diagrams/{filename}.svg"
    
    # Create parent directories if they don't exist
    os.makedirs(os.path.dirname(WORKSPACE + puml_path), exist_ok=True)
    
    # Write the PlantUML content to the .puml file
    with open(WORKSPACE + puml_path, 'w', encoding='utf-8') as f:
      f.write(content)
      
    # Render the PlantUML content to SVG
    svg_content = render(content, format='svg')[0]
    
    # Write the SVG content to the specified file
    with open(WORKSPACE + svg_path, 'wb') as f:
      f.write(svg_content)
    
    return {
        'status': 'success',
        'message': f'PlantUML content successfully rendered to {svg_path} and source saved to {puml_path}.'
    }
  except IOError as e:
    return {
        'status': 'error',
        'error_message': f'Error writing file: {e}'
    }
  except Exception as e:
    return {
        'status': 'error',
        'error_message': f'Unexpected error rendering PlantUML content: {e}'
    }