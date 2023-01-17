#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
- Use requests package
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print("Your email is:", argv[2])
