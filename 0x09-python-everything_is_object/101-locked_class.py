#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevent the user from instantiatng new locked
    class attributes for anything called
    "first_name".
    """
    __slots__ = ["first_name"]
