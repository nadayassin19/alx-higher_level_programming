#!/usr/bin/python3
"""a module of a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """it's a class that inhertis from rectangle class

    Args:
        Rectangle (class): it's a super class of square class
    """
    def __init__(self, size):
        """initialize a square

        Args:
            size (int): suare size
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
