#!/usr/bin/python3
"""It's a module of a func that return true or false
"""


def inherits_from(obj, a_class):
    """it's a function that returns
    True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    Args:
        obj, a_class
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return (True)
    else:
        return (False)
