#1/usr/bin/python3
"""Defines load_from_json_file function."""


import json
"""importing JSON library."""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        The object represented by the JSON file.
    """
    with open(filename) as file:
        return (json.load(file))
