#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import URLError
    from sys import argv

    req = Request(argv[1])
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'code'):
            print("Error code: ", e.code)
