#!/usr/bin/python3
"""It's a module of a rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class inhertits from BaseGeaometry class

    Args:
        BaseGeometry (class): the super class
    """
    def __init__(self, width, height):
        """initialization of rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
