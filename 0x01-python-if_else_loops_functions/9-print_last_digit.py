#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print(last_digit)
    return last_digit

def test_print_last_digit():
    output = print_last_digit(98)
    assert output == 8, f"Expected: 8, Got: {output}"

    output = print_last_digit(98)
    assert output == 8, f"Expected: 8, Got: {output}"

    output = print_last_digit(-98)
    assert output == 8, f"Expected: 8, Got: {output}"

    output = print_last_digit(0)
    assert output == 0, f"Expected: 0, Got: {output}"

test_print_last_digit()
