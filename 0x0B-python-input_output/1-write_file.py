#!/usr/bin/python3
"""Defines function to write to a file"""


def write_file(filename="", text=""):
    """Writes a string to text file
    Args:
        filename: file to store string
        text: text to be written to file

    Return: number of characters written
    """
    with open(filename, 'w', encoding='UTF-8') as myFile:
        return (myFile.write(text))
