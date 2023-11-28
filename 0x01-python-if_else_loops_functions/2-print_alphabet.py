#!/usr/bin/python3

def print_alphabet():
    for c in range(ord('a'), ord('z') + 1):
        print("{}".format(chr(c)), end='')


# Call the function to print the alphabet
print_alphabet()
