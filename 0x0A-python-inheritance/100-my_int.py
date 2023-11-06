#!/usr/bin/python3
"""A module of a class that inherits from int
"""


class MyInt(int):
    """a class that inherits from int
    & invert int operators == and !=.
    """

    def __eq__(self, value):
        """a method that returns != check
        """
        return (self.real != value)

    def __ne__(self, value):
        """a method that returns == check
        """
        return (self.real == value)
