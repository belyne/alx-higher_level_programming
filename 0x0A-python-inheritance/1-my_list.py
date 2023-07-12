#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).

        This method modifies the list in-place and does not
        return any value.
        """
        self.sort()
        print(self)
