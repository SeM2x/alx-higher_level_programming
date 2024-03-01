#!/usr/bin/python3
"""defines from_json_string function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): object
        filename (string): string
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
