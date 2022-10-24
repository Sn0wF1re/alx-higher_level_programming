#!/usr/bin/python3
"""Define function to add new attribute to object"""


def add_attribute(obj, name, val):
    """
    add attribute to object

    Args:
        obj: object to be given attribute
        name: attribute
        val: value of attribute
    TypeError: if can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
