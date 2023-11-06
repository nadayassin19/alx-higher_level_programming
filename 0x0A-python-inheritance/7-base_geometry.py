#!/usr/bin/python3
"""It's a module of a class
"""


class BaseGeometry:
    """It's a class of geometry
    """
    def __init__(self):
        """initialize a base geometry
        """
        pass

    def area(self):
        """not implemented method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates value

        Args:
            name (string), value (int).
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
