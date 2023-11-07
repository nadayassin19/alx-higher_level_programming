#!/usr/bin/python3
"""a module of a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): file name.
        search_string (str): string to be searched for.
        new_string (str): string to be appended.
    """
    ins_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            ins_line += [line]
            if line.find(search_string) != -1:
                ins_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(ins_line))
