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

    @staticmethod
    def from_json_string(json_string):
        """Returns list of json string representation"""
        if not json_string or json_string is None:
            return("[]")
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        if list_objs is None:
            with open(cls.__name__ + '.json', 'w', encoding='utf-8') as myFile:
                myFile.write('[]')

        else:
            list_insts = [x.to_dictionary() for x in list_objs]
            with open(cls.__name__ + '.json', 'w', encoding='utf-8') as myFile:
                myFile.write(cls.to_json_string(list_insts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            new = cls(69, 69)
        elif cls.__name__ == "Square":
            new = cls(69)
        else:
            new = None
        new.update(**dictionary)
        return (new)
