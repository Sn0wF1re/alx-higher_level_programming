#!/usr/bin/python3
"""Defines function to return dictionary description"""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure
    for json serialization of an object"""
    return obj.__dict__
