#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

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

    def area():
        """Returns the area of the reclangle"""
        return __width * __height

    def __str__():
        """Returns a string representing rectangle description"""
        return f'[Rectangle] {__width}/{__height}'
