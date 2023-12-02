#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find biggest integer in list"""
    if len(my_list) == 0:
        return (None)
    tmp = my_list[0]
    for item in my_list:
        if item > tmp:
            tmp = item

    return tmp
