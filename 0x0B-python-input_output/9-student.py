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

    def to_json(self):
        """retrieves a dictionary representation of
        a Student instance

        Returns:
            dict: dict representaion of an object
        """
        return self.__dict__
