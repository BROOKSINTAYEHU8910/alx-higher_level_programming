#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            separator = ", " if i < 8 or (i == 8 and j == 9) else "\n"
            print("{:d}{:d}".format(i, j), end=separator)
    if i == 8:
        print()  # Print a newline after the last iteration of the outer loop
