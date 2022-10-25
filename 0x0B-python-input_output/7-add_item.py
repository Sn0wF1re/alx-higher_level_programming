#!/usr/bin/python3
"""Add all arguments to a Python list and saves them to a file."""
import sys


if __name__ == "__main__":
    savetoJson = __import__('5-save_to_json_file').save_to_json_file
    jsonLoad = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = jsonLoad("add_item.json")
    except FileNotFoundError:
        items = list()
    items.extend(sys.argv[1:])
    savetoJson(items, "add_item.json")
