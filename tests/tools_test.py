import os
import pytest
from marc import tools

MARC_WORKSPACE_PATH = tools.MARC_WORKSPACE_PATH

def setup_module(module):
    # Ensure test directory exists
    os.makedirs(MARC_WORKSPACE_PATH, exist_ok=True)

def teardown_module(module):
    # Clean up test files
    test_file = os.path.join(MARC_WORKSPACE_PATH, "testfile.txt")
    if os.path.exists(test_file):
        os.remove(test_file)

def test_write_file_success():
    result = tools.write_file("Hello, world!", "testfile.txt")
    assert result == "Successfully wrote file"
    assert os.path.exists(os.path.join(MARC_WORKSPACE_PATH, "testfile.txt"))

def test_read_file_success():
    tools.write_file("Read this!", "testfile.txt")
    content = tools.read_file("testfile.txt")
    assert content == "Read this!"

def test_write_file_error():
    # Try writing to a directory that doesn't exist
    result = tools.write_file("fail", "nonexistent_dir/testfile.txt")
    assert result.startswith("Error writing file")

def test_read_file_error():
    # Try reading a file that doesn't exist
    result = tools.read_file("doesnotexist.txt")
    assert result.startswith("Error reading file")

def test_generate_puml_diagram():
    result = tools.generate_puml_diagram("@startuml\n@enduml")
    assert result == "Successfully generated the desired diagram!"

def test_discover_filesystem():
    # Should return a dict with at least the testfile.txt if it exists
    tools.write_file("abc", "testfile.txt")
    fs = tools.discover_filesystem()
    assert isinstance(fs, dict)
    assert "testfile.txt" in fs or any("testfile.txt" in v for v in fs.values() if isinstance(v, dict))
