#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/user"
    r = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
