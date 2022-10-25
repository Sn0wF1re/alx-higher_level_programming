#!/usr/bin/python3
"""Defines function that returns JSON representation of object"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    return (json.dumps(my_obj))
