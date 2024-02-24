#!/usr/bin/python3
"""Defines a class that inhertis from list"""


class MyList(list):
    """class that inhertis from list."""
    def print_sorted(self):
        """prints the sorted list."""
        print(sorted(self))
