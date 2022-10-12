#!/usr/bin/python3
"""Make a class square."""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """Initialize the new square.
        Args:
            size (int): Size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Set current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
