#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string in the format '[Square] <size>/<size>'.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
