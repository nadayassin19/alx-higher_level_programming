#!/usr/bin/python3
"""It's a module of a func that return true or false
"""


def is_kind_of_class(obj, a_class):
    """It's a function that returns
    True if the object is an instance of,
    or if the object is an instance of
    a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj, a_class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
