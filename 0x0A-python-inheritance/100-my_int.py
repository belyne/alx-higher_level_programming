#!/usr/bin/python3
"""
Defines a MyInt class that inherits from int.
"""

class MyInt(int):
    """
    Represents a rebel integer.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other: The value to compare against.

        Returns:
            True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other: The value to compare against.

        Returns:
            True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
