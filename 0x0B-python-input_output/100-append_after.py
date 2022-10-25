#!/usr/bin/python3
"""Defines an append function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string
    Args:
        filename: text file
        search_string: append after the string
        new_string: string to be appended after search_string
    """
    content = ""
    with open(filename, encoding='utf-8') as myFile:
        for line in myFile:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(content)
