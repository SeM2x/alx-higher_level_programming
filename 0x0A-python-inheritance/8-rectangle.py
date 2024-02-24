#!/usr/bin/python3
"""Defines a rectangle class that inherits from BaseGeometry class"""


class Rectangle(BaseGeometry):
    """rectangle class"""
    __width = 0
    __height = 0

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        __width = width
        __height = height
