#!/usr/bin/python3
import dis
import importlib.util
import sys

def print_hidden_names(file_path):
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <path to hidden_4.pyc>")
        sys.exit(1)

    file_path = sys.argv[1]
    print_hidden_names(file_path)
