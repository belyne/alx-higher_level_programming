#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save
them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == "__main__":
    # Load existing items from the file if it exists
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add new items from command line arguments
    items.extend(sys.argv[1:])

    # Save the updated items to the file
    save_to_json_file(items, "add_item.json")
