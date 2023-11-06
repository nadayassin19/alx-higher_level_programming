#!/usr/bin/python3
"""A module of a class that inherits from list
"""


class MyList(list):
    """It's a class that iherits from list

    Args:
        list (class): class list
    """
    def print_sorted(self):
        """a method that prints the list, but sorted (ascending sort)
        """
        print(self.sort())
