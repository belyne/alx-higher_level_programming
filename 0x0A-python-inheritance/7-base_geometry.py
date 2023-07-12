#!/usr/bin/python3
"""Defines BaseGeometry class."""


class BaseGeometry:
    """
    A base class representing basic geometry.

    This class provides methods for calculating area
    and validating integers.
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            NotImplementedError: Always raises an exception with
            the message 'area() is not implemented'.
        """
        raise NotImplementedError('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name: The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
