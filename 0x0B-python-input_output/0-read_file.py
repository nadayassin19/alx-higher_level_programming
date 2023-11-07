#!/usr/bin/python3
"""a module of a function that reads a text file
"""


def read_file(filename=""):
    """it's a function that reads a text file (UTF8)
    and prints it to stdout.

    Args:
        filename (str): file name.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
