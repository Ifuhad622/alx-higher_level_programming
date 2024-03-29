#!/usr/bin/python3
"""
Take in URL, send request to URL, and display value
of X-Request-Id variable in HTTPS response header
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
