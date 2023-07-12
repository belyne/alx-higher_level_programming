#!/usr/bin/python3
"""Defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class
        or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
