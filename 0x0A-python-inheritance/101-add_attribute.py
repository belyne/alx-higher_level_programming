#!/usr/bin/python3
"""
Defines a function to add a new attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
