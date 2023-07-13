#!/usr/bin/python3
"""Defines read_file function."""


def read_file(filename=""):
    """
    Reads the content of a text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read
        (default is an empty string).

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
