#!/usr/bin/python3
"""Defines function that returns object from json representation"""
import json


def from_json_string(my_str):
    """Returns object reresented by json string representation"""
    return (json.loads(my_str))
