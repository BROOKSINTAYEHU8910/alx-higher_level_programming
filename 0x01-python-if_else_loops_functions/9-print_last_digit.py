#!/usr/bin/python3
def print_first_digit(number):
    if number < 0:
        first_digit = int(str(-number)[0])
    elif number >= 0:
        first_digit = int(str(number)[0])
    print("{:d}".format(first_digit), end="")
    return first_digit
