#!/usr/bin/python3
"""A module of function that prints a square"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): The square size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
