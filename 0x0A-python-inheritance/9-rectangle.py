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
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """a method that calculates area

        Returns:
            int: rectangle area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """a method returns a string representation
        of a rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
