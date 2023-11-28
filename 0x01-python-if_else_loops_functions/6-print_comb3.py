#!/usr/bin/python3
combinations = []

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            combinations.append("{:d}{:d}".format(i, j))

print(", ".join(combinations))
