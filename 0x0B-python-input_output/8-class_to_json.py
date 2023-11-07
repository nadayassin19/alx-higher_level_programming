#!/usr/bin/python3
"""it's a module of a function that returns
the dictionary description with simple data structure
"""


def class_to_json(obj):
    """it's a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object.

    Args:
        obj: object to be represented in a dictionary description.
    """
    return (obj.__dict__)
