#!/usr/bin/python3
"""Defines a function to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div
    and returns a new matrix.

    Args:
        matrix: list of ints or floats
        div: Integer or float

    Raises:
        TypeError: if list is not ints or floats
        TypeError: if rows of matrix are not of same size
        TypeError: if div is a non-number
        ZeroDivisionError: if div is 0

    Return: New matrix with quotients
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(col, int) or isinstance(col, float))
                for col in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
