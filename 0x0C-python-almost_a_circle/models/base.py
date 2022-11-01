#!/usr/bin/python3
"""Create Class Base"""
import json
import os
import csv


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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        myList = list()
        myFile = cls.__name__ + ".json"
        if not os.path.isfile(myFile):
            return ([])
        else:
            with open(myFile, 'r', encoding='utf-8') as file:
                x = cls.from_json_string(file.read())
            for i in x:
                myList.append(cls.create(**i))
            return (myList)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
