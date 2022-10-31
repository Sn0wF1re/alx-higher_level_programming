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

    def __str__(self):
        """String representation overriding Base class"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args):
            i = 0
            for item in args:
                if i == 0:
                    if item is not None:
                        self.id = item
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                if i == 1:
                    self.width = item
                if i == 2:
                    self.height = item
                if i == 3:
                    self.x = item
                if i == 4:
                    self.y = item
                i += 1
        elif kwargs and len(kwargs):
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of class Rectangle"""
        return({'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y})
