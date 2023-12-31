#!/usr/bin/python3
"""square module that defines a module by its size
"""


class Square:
    """It's a class that defines a square by size.
    """
    def __init__(self, size=0):
        """initialize size

        Args:
            size (int): square size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
