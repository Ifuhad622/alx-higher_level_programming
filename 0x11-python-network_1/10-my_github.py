#!/usr/bin/python3
"""
Takes GitHub credentials (username and password),
uses GitHub API to display user id
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    json = response.json()

    print(json.get('id'))
