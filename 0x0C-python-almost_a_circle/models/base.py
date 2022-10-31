#!/usr/bin/python3
"""Create Class Base"""
import json


class Base:
    """Define the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
