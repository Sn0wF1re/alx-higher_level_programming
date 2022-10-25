#!/usr/bin/python3
"""Defines a function to write to file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using json representation
    Args:
        my_obj: object to be written
        filename: storage destination
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
