#!/usr/bin/python3
"""Defines Student class."""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None, retrieves all attributes. Default is None.

        Returns:
            dict: A dictionary containing the requested student attributes.
        """
        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']
        return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a
        dictionary.

        Args:
            json (dict): A dictionary representing the attributes
            of the student.
                The keys are the attribute names and the values are
                the attribute values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
