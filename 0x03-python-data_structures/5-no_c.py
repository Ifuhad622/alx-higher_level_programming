#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all c and C characters in string"""
    new_string = ""
    for item in my_string:
        if item == "c" or item == "C":
            continue
        new_string += item
    return new_string
