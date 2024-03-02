#!/usr/bin/python3
"""defines a Base class"""


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
            self.__nb_objects += 1
            self.id = self.__nb_objects
