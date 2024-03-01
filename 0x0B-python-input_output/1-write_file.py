#!/usr/bin/python3
"""defines a write_file function"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): file's name. Defaults to "".
        text (str, optional): text to write in the file. Defaults to "".
    """
    with open(filename, 'w') as f:
        return f.write(text)
