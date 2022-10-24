#!/usr/bin/python3
"""Define function to add new attribute to object"""


def add_attribute(obj, name, value):
    """
    add attribute to object

    Args:
        obj: object to be given attribute
        att: attribute
        value: value of attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add attribute")
    obj.__setattr__(name, value)
