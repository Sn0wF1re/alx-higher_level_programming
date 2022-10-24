#!/usr/bin/python3
"""Creates 'is_same_class' function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
    of the specified class ; otherwise False

    Args:
        obj: object to be checked
        a_class: The class to be checked against

    Returns: True if obj is instance of a_class
             False otherwise
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
