#!/usr/bin/python3

def print_last_digit(number):
    # Ensure the input is a valid integer
    if not isinstance(number, int):
        print("Please provide a valid integer.")
        return None

    # Take the absolute value to handle negative numbers
    number = abs(number)

    # Get the last digit
    last_digit = number % 10

    # Print the last digit
    print("Last digit:", last_digit)

    # Return the value of the last digit
    return last_digit
