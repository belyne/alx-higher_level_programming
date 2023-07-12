#!/usr/bin/python3
"""Defines Rectangle class."""


class BaseGeometry:
    """
    A base class representing basic geometry.

    This class provides methods for calculating area and validating integers.
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            NotImplementedError: Always raises an exception with the message 'area() is not implemented'.
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class and adds width and height properties.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
