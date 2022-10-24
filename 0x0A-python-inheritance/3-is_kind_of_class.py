#!/usr/bin/python3
"""Creates function to check if object
is an instance of inherited class
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance of a class

    Args:
        obj: object to be checked
        a_class: class which object is to be checked against

    Returns: True if object is an instance of a_class
             False otherwise
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
