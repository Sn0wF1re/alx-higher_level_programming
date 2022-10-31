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
