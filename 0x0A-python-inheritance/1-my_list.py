#!/usr/bin/python3
"""Creates an inherited list class MyList."""


class MyList(list):
    """extends list to print list in ascending order"""

    def print_sorted(self):
        """Print a sorted list in ascending order."""
        print(sorted(self))
