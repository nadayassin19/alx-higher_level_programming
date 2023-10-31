#!/usr/bin/python3
"""A module of function that finds the max int
"""


def max_integer(list=[]):
    """A function that finds and return the max integer.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
