#!/usr/bin/python3

"""This is a module to add two given integers
"""


def add_integer(a, b=98):
    """It's a function that adds 2 integers.

    Args:
        a (int): first integer.
        b (int): second integer. Defaults to 98.
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
