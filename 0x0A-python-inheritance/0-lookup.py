#!/usr/bin/python3
"""A module of a function def lookup(obj):
"""


def lookup(obj):
    """It's a function that returns the list
    of available attributes and methods of an object

    Args:
        obj (class):  list of available attributes and methods of an object
    """
    return (dir(obj))
