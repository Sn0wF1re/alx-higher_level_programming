#!/usr/bin/python3
"""Unittests for max_integer([...])."""


import unittest
max_integer = __import__('6-max_integer.py').max_integer


class TestMaxInteger(unittest.TestCase):
    """Create unittests for max_integer([...])"""


    def test_ordered_list(self):
        """Ordered list of integers."""
        my_list = [1, 2, 3]
        self.assertEqual(max_integer(my_list), 3)

    def test_unordered_list(self):
        """Unordered list of integers."""
        my_list = [1, 3, 7, 6]
        self.assertEqual(max_integer(my_list), 7)

    def test_beginning(self):
        """List with a max value at index 0."""
        my_list = [8, 7, 6, 5]
        self.assertEqual(max_integer(my_list), 8)

    def test_empty_list(self):
        """Test for an empty list."""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_one_element(self):
        """Test a list with one element."""
        my_list = [4]
        self.assertEqual(max_integer(my_list), 4)

    def test_floats(self):
        """For a list with floats."""
        my_list = [0.6, 7.67, -20.69, 69.0, 4.20]
        self.assertEqual(max_integer(my_list), 69.0)

    def test_mixed(self):
        """Test case for list of ints and floats."""
        my_list = [0.6, 7.67, -7, 69, 6]
        self.assertEqual(max_integer(my_list), 69)

    def test_string(self):
        """case for a string."""
        string = "Newton"
        self.assertEqual(max_integer(string), 'w')

    def test_string_list(self):
        """Case for a list of strings."""
        my_list = ["Newton", "and", "Clinton", "here"]
        self.assertEqual(max_integer(my_list), "Newton")

    def test_empty_string(self):
        """Test for an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
