#!/usr/bin/python3
"""a module of a class square that inherits from
a class rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class square

    Args:
        Rectangle (class): super class that the class square
        inherits from.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new square

        Args:
            size (int): the square size
            x (int, optional): the square x coordinate, Defaults to 0.
            y (int, optional): the square y coordinate, Defaults to 0.
            id (int): the square id Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """a method that returns the square location and its dimensions
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """a method to retrieve size
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """a method to set size value

        Args:
            value (int): size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """a method that assigns an argument to each attribute,
        here, the number of attributes is unknown.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
