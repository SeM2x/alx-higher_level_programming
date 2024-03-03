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
        list_dicts = []
        if list_objs:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str):  a string representing a list of dictionaries

        Returns:
            dict: list represented by json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Returns:
            object: a Base instance
        """
        if cls.__name__ == 'Square':
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        try:
            with open(f'{cls.__name__}.json', 'r') as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        objs = []
        for obj in cls.from_json_string(json_string):
            objs += [cls.create(**obj)]

        return objs
