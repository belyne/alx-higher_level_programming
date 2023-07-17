#!/usr/bin/python3
"""
Defines a function to load an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
