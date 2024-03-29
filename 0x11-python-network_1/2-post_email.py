#!/usr/bin/python3
"""
Takes in url, sends POST request to URL with specific
email as parameter, and displays HTTPS (UTF-8) response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    DATA = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, DATA)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
