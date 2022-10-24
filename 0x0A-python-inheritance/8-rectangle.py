#!/usr/bin/python3
"""Creates inherited class 'Rectangle'"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """Inherits the class BaseGeometry"""

    def __init__(self, width, height):
        """Initializes width and height

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
