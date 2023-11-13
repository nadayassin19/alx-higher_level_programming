#!/usr/bin/python3
"""a module of a class (base)
"""


class Base:
    """a class called base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance

        Args:
            id (int).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
