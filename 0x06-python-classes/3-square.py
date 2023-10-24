#!/usr/bin/python3
"""a square module that defines a square by its size and gets its area"""


class Square:
    """It's a class that defines a suare by size & area
    """
    def __init__(self, size=0):
        """initialze size

        Args:
            size (int): square size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """it's a method that returns the current square area.
        """
        return (self.__size ** 2)
