#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is between 97 and 122
    return ord(c) >= 97 and ord(c) <= 122

# Test cases
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

