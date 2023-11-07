#!/usr/bin/python3
"""a module of a function writes an object to text file.
"""


import json


def save_to_json_file(my_obj, filename):
    """it's a function that writes an Object
    to a text file, using a JSON representation

    Args:
        my_obj: object to be saved
        filename (str): the file to be saved
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
