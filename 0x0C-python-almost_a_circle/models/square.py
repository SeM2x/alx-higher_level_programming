#!/usr/bin/python3
"""defines a Square class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y}' \
            f' - {self.size}'

    @property
    def size(self):
        """size getter

        Returns:
            int: size of the Square
        """
        return self.width

    @size.setter
    def size(self, size):
        """size setter

        Args:
            size (int): size of the Square
        """
        self.width = size
        self.height = size
