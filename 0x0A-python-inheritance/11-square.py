#!/usr/bin/python3
"""creates class that inherits Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size):
        """instantiates square size"""
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns string representation"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
