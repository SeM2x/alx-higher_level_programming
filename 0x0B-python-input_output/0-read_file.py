#!/usr/bin/python3
"""defines a read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): the file's name. Defaults to "".
    """
    with open(filename, 'r') as f:
        print(f.read())
