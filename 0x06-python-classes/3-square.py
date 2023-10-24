#!/usr/bin/python3
class Square:
    """It's a class that defines a suare by size & area
    """
    def __init__(self, size=0):
        """initialze size

        Args:
            size (int): square size.
        """
        if type(size) != int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
    
    def area(self):
        """it's a method that returns the current square area.
        """
        self.area = self.__size ** 2
        return (self.area)
