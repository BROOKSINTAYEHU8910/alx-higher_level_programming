#!/usr/bin/python3

def remove_char_at(my_str, n):
    # Check if the index is valid
    if 0 <= n < len(my_str):
        # Create a copy of the string with the character at position n removed
        result = my_str[:n] + my_str[n+1:]
        return result
    else:
        # If the index is out of bounds, return the original string
        return my_str
