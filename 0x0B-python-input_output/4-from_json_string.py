#!/usr/bin/python3
"""defines from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (string): a JSON string

    Returns:
        object: object representation of my_str
    """
    return json.loads(my_str)
