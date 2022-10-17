#!/usr/bin/python3
"""Defines a function to print a square"""


def print_square(size):
    """Prints the # character

    Args:
        size: height and width of square.

    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and < 0
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
