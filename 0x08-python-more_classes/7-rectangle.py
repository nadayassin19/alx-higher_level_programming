#!/usr/bin/python3
"""A module to define a rectangle
"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
    number_of_instances (int): the no. of rectangle instances.
    print_symbol (any): used for stinf represntation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a new rectangle

        Args:
            width (int): rectangle width. Defaults to 0.
            height (int): rectangle height. Defaults to 0.
        """
        type(self).number_of_instances += 1
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
        if (self.__width or self.__height) == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """a method that prints the rectangle with the character #

        Returns:
            str: a rectangle represented by #
        """
        if (self.__width or self.__height) == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """a method that returns a string representation
        of the rectangle to be able to
        recreate a new instance by using eval()

        Returns:
            str: a string representation of a rectangle.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message when the rectangle is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
