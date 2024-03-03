#!/usr/bin/python3
"""defines a Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation method

        Args:
            id (str, optional): id of the object. Defaults to None.
        """
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            str: string representation of list_dictionaries
        """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of objects
        """
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(cls.to_json_string(list_dicts))
