#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing pascal's triangle of n
    Args:
        n (int): represents Pascal's triangle
    Returns: list of lists
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
