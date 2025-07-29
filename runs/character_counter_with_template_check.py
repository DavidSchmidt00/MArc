import os
import glob
import filecmp

def are_files_identical(file1, file2):
    """
    Compares two files to see if they are identical.
    """
    if not os.path.exists(file2):
        return False
    return filecmp.cmp(file1, file2, shallow=False)

def count_characters_in_run(run_path, template_base_path):
    """
    Counts the total characters in all .adoc and .puml files within a specific run directory,
    excluding files that are identical to the template.
    """
    total_chars = 0
    files_to_process = []
    for ext in ('**/*.adoc', '**/*.puml'):
        files_to_process.extend(glob.glob(os.path.join(run_path, ext), recursive=True))

    for file_path in files_to_process:
        relative_path = os.path.relpath(file_path, run_path)
        template_file_path = os.path.join(template_base_path, relative_path)

        if are_files_identical(file_path, template_file_path):
            print(f"  - Skipping identical file: {relative_path}")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                total_chars += len(content)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            
    return total_chars

def main():
    """
    Main function to iterate through LLM and run directories,
    calculate character counts, and write them to a file.
    """
    runs_dir = 'runs'
    template_dir = 'template/architecture template long'
    
    if not os.path.isdir(runs_dir):
        print(f"Directory '{runs_dir}' not found.")
        return
    if not os.path.isdir(template_dir):
        print(f"Template directory '{template_dir}' not found.")
        return

    for llm_folder in os.listdir(runs_dir):
        llm_path = os.path.join(runs_dir, llm_folder)
        if os.path.isdir(llm_path):
            for run_folder in os.listdir(llm_path):
                run_path = os.path.join(llm_path, run_folder)
                if os.path.isdir(run_path):
                    print(f"Processing: {run_path}")
                    total_chars = count_characters_in_run(run_path, template_dir)
                    
                    output_file_path = os.path.join(run_path, "character_count_corrected.txt")
                    try:
                        with open(output_file_path, 'w', encoding='utf-8') as f:
                            f.write(str(total_chars))
                        print(f"  -> Wrote {total_chars} characters to {output_file_path}")
                    except Exception as e:
                        print(f"  -> Error writing to file {output_file_path}: {e}")

if __name__ == "__main__":
    main()
