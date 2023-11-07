#!/usr/bin/python3
"""a module of a function that writes a string
to text file
"""


def write_file(filename="", text=""):
    """it's a function that writes a string
    to a text file (UTF8) and returns
    the number of characters written.

    Args:
        filename (str): given file name.
        text (str): the text to be written.
    """
    lines = 0
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
