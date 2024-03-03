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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if (kwargs):
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            attrs = ['id', 'size', 'x', 'y']
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)

    def to_dictionary(self):
        """returns the dictionary representation of a Square

        Returns:
            dict: the sdictionary representation of a Square
        """
        new_dict = {}
        for key, val in self.__dict__.items():
            key = key.replace('_Rectangle__', '')
            if key == 'width' or key == 'height':
                new_dict['size'] = val
            else:
                new_dict[key] = val
        return new_dict
