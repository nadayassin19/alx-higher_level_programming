#!/usr/bin/python3
"""A module to define a rectangle
"""


class Rectangle:
    """A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """initialize a new rectangle

        Args:
            width (int): rectangle width. Defaults to 0.
            height (int): rectangle height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a method to retrieve the rectangle width.
        """
        return (self._width)

    @width.setter
    def width(self, value):
        """a method to set the rectangle width

        Args:
            value (value): width value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a method to retrieve the rectangle height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """a method to set the rectangle width

        Args:
            value (int): height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """a method that returns rectangle area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """a method that returns rectabgle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height + self.__width) * 2)
