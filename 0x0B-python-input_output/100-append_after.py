#!/usr/bin/python3
"""
Defines a function to append a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each matched line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)