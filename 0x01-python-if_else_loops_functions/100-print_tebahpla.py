#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(i - 32 if (122 - i) % 4 < 2 else i), end="")
