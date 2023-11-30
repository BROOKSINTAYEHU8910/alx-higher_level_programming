#!/usr/bin/python3
if __name__ == "__main__":
    import secret_module_42
    # Print names sorted in alphabetical order
    for name in sorted(dir(secret_module_42)):
        # Print only names that do not start with __
        if not name.startswith("__"):
            print("{}".format(name))
