#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds a peak of unsorted integers
    """
    listLength = len(list_of_integers)
    if not list_of_integers:
        return (None)
    if listLength == 1:
        return list_of_integers[0]
    if listLength == 2:
        return max(list_of_integers)
    middle = int(listLength / 2)
    peak = list_of_integers[middle]
    if peak > list_of_integers[middle - 1]\
            and peak > list_of_integers[middle + 1]:
        return peak
    elif list_of_integers[middle - 1] > peak:
        return (find_peak(list_of_integers[:middle]))
    else:
        return (find_peak(list_of_integers[middle + 1:]))
