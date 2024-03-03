#!/usr/bin/python3
"""defines a Rectangle class"""
from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter

        Returns:
            int: width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter

        Args:
            width (int): width of the Rectangle
        """
        self.__width = width

    @property
    def height(self):
        """height getter

        Returns:
            int: height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter

        Args:
            height (int): height of the Rectangle
        """
        self.__height = height

    @property
    def x(self):
        """x getter

        Returns:
            int: x of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter

        Args:
            x (int): x of the Rectangle
        """
        self.__x = x

    @property
    def y(self):
        """y getter

        Returns:
            int: y of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter

        Args:
            y (int): y of the Rectangle
        """
        self.__y = y
