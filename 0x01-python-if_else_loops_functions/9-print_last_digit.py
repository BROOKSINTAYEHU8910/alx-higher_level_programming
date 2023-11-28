#!/usr/bin/python3

def print_last_digit(number):
    if not isinstance(number, int):
        print("Please provide a valid integer.")
        return None

    number = abs(number)
    last_digit = number % 10
    print("Last digit:", last_digit)
    return last_digit
