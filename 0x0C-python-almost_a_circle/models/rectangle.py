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
        if (type(width) is not int):
            raise TypeError(f'width must be an integer')
        if (width <= 0):
            raise ValueError(f'width must be > 0')
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
        if (type(height) is not int):
            raise TypeError(f'height must be an integer')
        if (height <= 0):
            raise ValueError(f'height must be > 0')
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
        if (type(x) is not int):
            raise TypeError(f'x must be an integer')
        if (x < 0):
            raise ValueError(f'x must be >= 0')
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
        if (type(y) is not int):
            raise TypeError(f'y must be an integer')
        if (y < 0):
            raise ValueError(f'y must be >= 0')
        self.__y = y

    def area(self):
        """calculates the area value of the Rectangle instance.

        Returns:
            int: the area value of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        print(self.y * '\n', end='')
        for i in range(self.height):
            print(f'{self.x * " "}', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y}' \
            f' - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if (kwargs):
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)
