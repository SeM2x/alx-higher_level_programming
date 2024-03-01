#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method

        Args:
            first_name (string): first_name
            last_name (string): last_name
            age (number): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance

        Args:
            attrs (list): list of attributes to be retrieved
        Returns:
            dict: dict representaion of an object
        """
        if (isinstance(attrs, list)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (dict): json
        """
        for key, value in json.items():
            setattr(self, key, value)
