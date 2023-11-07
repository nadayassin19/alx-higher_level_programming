#!/usr/bin/python3
"""a module of a function returns an object (Python data structure)
"""


import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): text to be converted from json to python data
    """
    return (json.loads(my_str))
