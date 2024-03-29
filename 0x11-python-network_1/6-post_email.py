#!/usr/bin/python3
"""
Take in URL, send request to URL and display
X-Request-Id value in response header.
"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
