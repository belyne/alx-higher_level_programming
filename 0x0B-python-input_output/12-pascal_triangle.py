#!/usr/bin/python3
"""Defines pascal_triangle function."""


def pascal_triangle(n):
    """
    Returns the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(row)

    return triangle
