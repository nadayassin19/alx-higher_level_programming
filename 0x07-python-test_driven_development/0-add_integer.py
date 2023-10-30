#!/usr/bin/python3

"""This is a module to add two given integers
"""

def add_integer(a, b=98):
    """It's a function that adds 2 integers.

    Args:
        a (int): first integer.
        b (int): second integer. Defaults to 98.
    """
    if type(a) != (int or float):
        raise TypeError("a must be an integer")
    if type(b) != (int or float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)