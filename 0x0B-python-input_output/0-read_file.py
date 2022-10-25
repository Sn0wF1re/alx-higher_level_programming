#!/usr/bin/python3
"""Defines function read_file"""


def read_file(filename=""):
    """Reads text file and prints it to stdout"""
    with open(filename, encoding='UTF-8') as myFile:
        print(myFile.read(), end="")
