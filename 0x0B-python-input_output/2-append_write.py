#!/usr/bin/python3
"""a module of function appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """it's a function that appends
    a string at the end of a text file
    (UTF8) and returns the number of characters added.

    Args:
        filename (str): file name.
        text (str): the text to be written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
