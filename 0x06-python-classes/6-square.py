#!/usr/bin/python3
"""it's a square module that defines a square"""


class Square:
    """it's a class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize size

        Args:
            size (int): square size.
            position (tuple): square position.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """it's a property to retrieve the square size
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

    @property
    def position(self):
        """it's a property to retrieve the square position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """to set the positions value

        Args:
            value (tuple): position value
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
