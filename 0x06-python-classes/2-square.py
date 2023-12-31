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
