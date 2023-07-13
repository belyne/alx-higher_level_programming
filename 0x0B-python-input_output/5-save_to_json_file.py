#!/usr/bin/python3
"""Defines save_to_json_file function."""


import json
"""importing JSON library."""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to save to the file.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
