#!/usr/bin/python3
"""a module of a function creates an object from a json file
"""


import json


def load_from_json_file(filename):
    """it's a function that creates an Object from a “JSON file”

    Args:
        filename (str): the name of file to be used to create an object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
