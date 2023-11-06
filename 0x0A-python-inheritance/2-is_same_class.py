#!/usr/bin/python3
"""It's a module of a func that return true or false
"""


def is_same_class(obj, a_class):
    """it's a function that returns
    True if the object is exactly an
    instance of the specified class; otherwise False.

    Args:
        obj, a_class
    """
    return (type(obj) is a_class)
