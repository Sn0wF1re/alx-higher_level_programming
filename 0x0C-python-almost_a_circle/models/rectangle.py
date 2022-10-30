#!/usr/bin/python3
"""Creates Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validation('width', value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validation('height', value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validation('x', value, False)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validation('y', value, False)
        self.__y = value

    def validation(self, name, value, equal=True):
        """Validation of setter methods and instantiation"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if not equal and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif equal and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """Returns value area of Rectangle instance"""
        return (self.__height * self.__width)

    def display(self):
        """Prints in stdout Rectangle instance with # character"""
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n')
              * self.__height, end="")
