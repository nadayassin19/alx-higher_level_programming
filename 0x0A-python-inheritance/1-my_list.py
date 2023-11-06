#!/usr/bin/python3
"""Defines an inherited list class MyList.
"""


class MyList(list):
    """a class inherits from list
    """

    def print_sorted(self):
        """a method that prints a list in sorted ascending order.
        """
        req_list = self.copy()
        req_list.sort()
        print(req_list)
