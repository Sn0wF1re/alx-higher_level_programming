#!/usr/bin/python3
"""Write a class that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize new rectangle
        Args:
           width: width of rectangle
           height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Print the rectangle with # character"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))
