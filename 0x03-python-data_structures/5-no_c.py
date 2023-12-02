#!/usr/bin/python3

def no_c(my_string):
    # Using list comprehension to create a new string without 'c' and 'C'
    new_string = ''.join(char for char in my_string if char.lower() != 'c')

    return new_string
