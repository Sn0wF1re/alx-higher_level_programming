#!/usr/bin/python3
"""creates class Square to inherit from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of Square info"""
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.height}")

    @property
    def size(self):
        """size getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes through keyword or non-keyword args"""
        if not args and not kwargs:
            return
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for k, v in enumerate(args):
                if k < len(attrs):
                    setattr(self, attrs[k], v)
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                else:
                    if hasattr(self, k):
                        setattr(self, k, v)
