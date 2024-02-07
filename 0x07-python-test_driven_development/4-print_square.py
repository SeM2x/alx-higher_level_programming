#!/usr/bin/python3
"""function that prints a square with the character #."""


def print_square(size):
    """prints a square.
    Args:
        size: the size of the square
    Raises:
        TypeError: if size is not an integer
        ValurError: is size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
