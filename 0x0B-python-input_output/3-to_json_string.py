#!/usr/bin/python3
"""a module of a function that returns the JSON representation
"""


import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string).

    Args:
        my_obj: the data to be converted into json data.
    """
    return (json.dumps(my_obj))
