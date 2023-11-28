#!/usr/bin/python3
# 8-uppercase.py

"""Prints a string in uppercase"""


def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
