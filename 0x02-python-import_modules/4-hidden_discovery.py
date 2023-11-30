#!/usr/bin/python3
import dis
import py_compile
import sys
import tempfile
import os

def print_hidden_names(filename):
    # Create a temporary directory to store the compiled Python file
    with tempfile.TemporaryDirectory() as temp_dir:
        compiled_filename = os.path.join(temp_dir, "hidden_compiled.pyc")

        try:
            # Compile the source code and save the compiled file
            py_compile.compile(filename, cfile=compiled_filename)
            with open(compiled_filename, 'rb') as file:
                # Read the magic number and timestamp (8 bytes)
                file.read(8)
                # Read the rest of the file
                file_contents = file.read()

            # Disassemble the bytecode
            dis.dis(file_contents)
        except SyntaxError as e:
            print(f"Error compiling/disassembling {filename}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <source_module.py>")
        sys.exit(1)

    source_module_filename = sys.argv[1]
    print_hidden_names(source_module_filename)
