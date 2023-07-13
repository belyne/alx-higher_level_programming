#!/usr/bin/python3
"""Defines to_json_string function."""


import json
"""importing json for the file to be compiled."""


def to_json_string(my_obj):
    """Returns the JSON representation of an obj(string).

    args:
        my_obj : the object to convert to JSON.

    Returns:
          (str) : the JSON representation of an object.
    """
    return (json.dumps(my_obj))
