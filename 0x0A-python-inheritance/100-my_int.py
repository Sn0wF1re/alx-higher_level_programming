#!/usr/bin/python3
"""Create a class MyInt"""


class MyInt(int):
    """inverts == and != operators"""

    def __eq__(self, value):
        """inverts == to !="""
        return (self.real != value)

    def __ne__(self, value):
        """inverts != with =="""
        return (self.real == value)

