#!/usr/bin/python3
import importlib.util
import dis
import sys

def print_hidden_names(filename):
    spec = importlib.util.spec_from_file_location("module_name", filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Extract names from the module
    names = [name for name in dir(module) if not name.startswith('__')]

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <compiled_module.pyc>")
        sys.exit(1)

    compiled_module_filename = sys.argv[1]
    print_hidden_names(compiled_module_filename)
