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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returs a string representation of a Square"""
        return f"[Square] {self.__size}/{self.__size}"
