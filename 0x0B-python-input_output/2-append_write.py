#!/usr/bin/python3
"""defines append_write function"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str, optional): file's name. Defaults to "".
        text (str, optional): text to append to the file. Defaults to "".
    """
    with open(filename, 'a') as f:
        return f.write(text)
