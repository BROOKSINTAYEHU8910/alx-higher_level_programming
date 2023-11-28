#!/usr/bin/python3
import random

number = random.randint(-10, 10)

print(f"The number is: {number}")

if number > 0:
    print(f"Correct output - {number} is positive")
elif number == 0:
    print(f"Correct output - {number} is zero")
else:
    print(f"Correct output - {number} is negative")

