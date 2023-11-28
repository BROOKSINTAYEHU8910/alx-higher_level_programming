#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)

# Print the assigned number
print(f"The number is: {number}")

# Check if the number is positive, negative, or zero, and print the corresponding message
if number > 0:
    print(f"Correct output - {number} is positive")
elif number == 0:
    print(f"Correct output - {number} is zero")
else:
    print(f"Correct output - {number} is negative")

