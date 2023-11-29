#!/usr/bin/python3
def pow(a, b):
    # Base case: anything to the power of 0 is 1
    if b == 0:
        return 1
    # Negative exponent case: a^(-b) is 1 / (a^b)
    elif b < 0:
        return 1 / pow(a, -b)
    # Recursive case: a^b = a * a^(b-1)
    else:
        return a * pow(a, b - 1)

