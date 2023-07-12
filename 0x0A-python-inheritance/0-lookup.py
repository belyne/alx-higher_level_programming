#!/usr/bin/python3
"""Defines looup function."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
