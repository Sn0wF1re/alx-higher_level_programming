#!/usr/bin/python3
"""Creates a function to add 2 integers"""

def add_integer(a, b=98):
    """Returns an integer after addition of a and b

    Raises:
        TypeError: if a or b is neither float nor integer
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
