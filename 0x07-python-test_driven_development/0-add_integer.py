#!/usr/bin/python3
# 0-add_integer.py
""" file name """


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Defaults to 98.

    Returns:
        int: The addition of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
          ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
          ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
