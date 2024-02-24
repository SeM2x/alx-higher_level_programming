#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size
