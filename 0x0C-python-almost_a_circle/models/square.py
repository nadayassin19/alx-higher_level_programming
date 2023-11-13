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
