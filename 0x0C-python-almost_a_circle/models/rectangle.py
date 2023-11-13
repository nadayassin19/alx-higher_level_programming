#!/usr/bin/python3
"""a module of a rectangle class"""
from base import Base


class Rectangle(Base):
    """a rectangle class

    Args:
        Base (class): the super class that the rectangle class inherits from.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
            x (int): x coordenate of the new rectangle, Defaults to 0.
            y (int): y coordenate of the new rectangle, Defaults to 0.
            id (int): the rectangle id, Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """to retrie the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """a method to set the width value

        Args:
            value (int): width value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """to retrie the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """a method to set the height value

        Args:
            value (int): height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """to retrie the x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """a method to set the x value

        Args:
            value (int): x value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to retrie the y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """a method to set the y value

        Args:
            value (int): y value
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """a method to get the area of the rectangle
        """
        return (self.width * self.height)

    def display(self):
        """a method that prints in stdout
        the Rectangle instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """a method that returns the rectangle location and its dimensions
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """a method that assigns an argument to each attribute,
        here, the number of attributes is unknown.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width,
                                      self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = k
                elif j == "width":
                    self.width = k
                elif j == "height":
                    self.height = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k
