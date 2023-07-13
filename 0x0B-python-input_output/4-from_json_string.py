#!/usr/bin/python3
"""Defines from_json_string function."""


import json
"""importing JSON for compilation ease."""


def from_json_string(my_str):
    """Returns an object(Python data structure) represented
    by JSON string.

    Args:
        my_str (str): JSON string representing onject.

    returns:
           (objt) (str): represented by JSON string.
    """
    return (json.loads(my_str))
