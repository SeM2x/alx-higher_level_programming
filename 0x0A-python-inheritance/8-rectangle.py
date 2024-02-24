#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    __width = 0
    __height = 0

    def __init__(self, width, height):
        super().__init__()
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator('width', width) 
        __width = width
        self.integer_validator('height', height)
        __height = height
