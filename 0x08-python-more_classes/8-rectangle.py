#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle area-wise"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Print the rectangle with # character"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """Returns string representation of Rectangle to be able
        to create a new instance by using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
