#!/usr/bin/python3
class Square:
    """it's a class that defines a square
    """
    def __init__(self, size=0):
        """initialize size

        Args:
            size (int): square size.
        """
        self.__size = size
    
    @property
    def size(self):
        """to retrieve the size
        """
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """to set the size value

        Args:
            value (int): size value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """square area
        """
        return (self.__size ** 2)
