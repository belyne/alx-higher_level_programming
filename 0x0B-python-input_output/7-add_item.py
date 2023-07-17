#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them
to a file in JSON format.
"""

import sys
from typing import List
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_list(filename: str, args: List[str]) -> List[str]:
    """
    Adds all arguments to a Python list and saves them
    to a file in JSON format.

    Args:
        filename (str): The name of the JSON file.
        args (List[str]): The arguments to add to the list.

    Returns:
        The updated list with the added arguments.
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)

    save_to_json_file(my_list, filename)

    return my_list


if __name__ == '__main__':
    filename = "add_item.json"
    args = sys.argv[1:]
    updated_list = add_to_list(filename, args)
    print(updated_list)
