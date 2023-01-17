#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request as request
    from urllib.error import HTTPError
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: ", e.code)
