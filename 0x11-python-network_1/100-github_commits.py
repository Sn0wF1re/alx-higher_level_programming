#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print("{}: {}".format(
            commits[i].get('sha'),
            commits[i].get('commit').get('author').get('name')
            ))
