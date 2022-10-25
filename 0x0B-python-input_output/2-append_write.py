#!/usr/bin/python3
"""Defines function append_write"""


def append_write(filename="", text=""):
    """Appends string at the end of text file
    Args:
        filename: text file
        text: string to be appended

    Return: Number of character added
    """
    with open(filename, 'a', encoding='UTF-8') as myFile:
        return (myFile.write(text))
