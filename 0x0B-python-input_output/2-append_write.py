#!/usr/bin/python3
"""Defines append_write function."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file(UTF8).

    args:
        filename (str): the name of the file to write.
        text (str): the text to write to the file.

    Returns:
           returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
