#!/usr/bin/python3
"""Define a Sqaure class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance"""
        self.size = size
        self.position = position

    def __str__(self):
        string = ""
        if self.__size == 0:
            string = "\n"
        else:
            for i in range(self.__position[1]):
                string += "\n"

        for i in range(self.__size):
            string += self.__position[0] * " "
            for j in range(self.__size):
                string += "#"
            if i < self.__size - 1:
                string += "\n"
        return string

    @property
    def size(self):
        """returns the private attribute size"""
        return self.__size

    @property
    def position(self):
        """returns the private attribute position"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets size to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """sets position to value"""

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            print(self.__position[0] * " ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
