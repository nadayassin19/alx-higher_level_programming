#!/usr/bin/python3
"""a module of a class defines a student
"""


class Student():
    """a class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """initialize a new student

        Args:
            first_name (str): new student fn
            last_name (str): new student ln
            age (int): new student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """it's a method that retrieves a dictionary
        representation of a Student instance
        """
        return (self.__dict__)
