#!/usr/bin/python3
"""it's a square module that defines a square by its size, are
& prints a square shape"""


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
        """it's a property to retrieve the square size
        """
        return (self.size)

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
        """return the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """a method that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#",end="")
                print()
