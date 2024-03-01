#!/usr/bin/python3
"""defines to_json_string function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (object): an object

    Returns:
        string: JSON representation of my_obj
    """
    return json.dumps(my_obj)
