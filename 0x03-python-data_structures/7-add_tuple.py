#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure that each tuple has at least two elements
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Add corresponding elements and create a new tuple
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple
