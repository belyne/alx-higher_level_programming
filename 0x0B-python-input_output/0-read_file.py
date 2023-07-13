#!/usr/bin/python3
"""Defines read_file function."""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
