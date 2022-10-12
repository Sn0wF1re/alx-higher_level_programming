#!/usr/bin/python3
"""Make a class square"""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """Initialize the new square.

        Args:
            size (int): size of new square.
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")
