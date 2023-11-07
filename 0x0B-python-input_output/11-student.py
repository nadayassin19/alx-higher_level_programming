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

    def to_json(self, attrs=None):
        """it's a method that retrieves a dictionary
        representation of a Student instance
        """
        obj = self.__dict__

        if type(attrs) == list:
            for item in attrs:
                if type(item) is not str:
                    return (obj)

            present_list = {}
            for item in range(len(attrs)):
                for strin in obj:
                    if attrs[item] == strin:
                        present_list[strin] = obj[strin]
            return (present_list)
        return (obj)

    def reload_from_json(self, json):
        """it's a method that replaces all attributes of the Student instance
        """
        for atr in json:
            self.__dict__[atr] = json[atr]
