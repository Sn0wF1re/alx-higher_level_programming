#!/usr/bin/python3
"""Defines function that creates an Object from a json file"""
import json


def load_from_json_file(filename):
    """creates object from json file"""
    with open(filename, encoding='utf-8') as myFile:
        return (json.load(myFile))
