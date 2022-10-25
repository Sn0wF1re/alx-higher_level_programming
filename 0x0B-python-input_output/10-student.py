#!/usr/bin/python3
"""Creates class Student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiates first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance
        """
        if type(attrs) == list and all(type(items) == str for items in attrs):
            return {val: getattr(self, val) for val
                    in attrs if hasattr(self, val)}
        return (self.__dict__)
