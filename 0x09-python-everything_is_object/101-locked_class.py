#!/usr/bin/python3
"""Defines class LockedClass"""


class LockedClass:
    """Prevents user from dynamically creating new instance attributes
    except if instance is called first_name
    """
    __slots__ = ['first_name']
