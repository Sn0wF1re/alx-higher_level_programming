#!/usr/bin/python3
"""Creates a function"""


def inherits_from(obj, a_class):
    """Checks whether object is an instance
    of an inherited class

    Args:
        obj: object to be checked
        a_class: class to be checked against

    Return: True if object is an instance of a_class
            False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
