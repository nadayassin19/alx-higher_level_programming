#!/usr/bin/python3
"""a module of a class (base)
"""
from fileinput import filename
import json
from queue import Empty


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: it's a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """it's a method that writes the JSON string
        representation of list_objs to a file

        Args:
            list_objs: is a list of instances who inherits of Base,
            it's supposed to be represented by json file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """it's a method that returns the list of the
        JSON string representation json_string

        Args:
            json_string: is a string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """a method that returns an instance with all attributes already set
        """
