#!/usr/bin/python3
"""Define a Sqaure class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __init__(self, size=0):
        """Initialize a square instance"""

        self.size = size

    @property
    def size(self):
        """returns the private attribute size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets size to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""

        return self.__size * self.__size
