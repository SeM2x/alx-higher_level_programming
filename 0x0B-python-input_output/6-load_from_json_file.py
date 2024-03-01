#!/usr/bin/python3
"""defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (string): string
    """
    with open(filename, 'r') as f:
        return json.load(f)
