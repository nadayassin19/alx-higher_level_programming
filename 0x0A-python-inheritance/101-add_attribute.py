#!/usr/bin/python3
"""A module of a funnc that add a new attribute
to an object
"""


def add_attribute(obj, name, value):
    """ a function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: attribute value
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
