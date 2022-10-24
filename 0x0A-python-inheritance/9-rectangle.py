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
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string representations of rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
