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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            str: string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)
