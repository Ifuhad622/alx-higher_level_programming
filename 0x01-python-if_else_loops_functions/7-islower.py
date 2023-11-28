#!/usr/bin/python3
# 7-islower.py

"""Checks for lowercase character"""


def islower(c):
    if 97 <= ord(c) <= 122:
        return True
    return False
