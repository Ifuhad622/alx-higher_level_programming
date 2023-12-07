#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    """Add all unique integers in list."""
    list_s = set(my_list)
    sum = 0
    for item in list_s:
        sum += item
    return summ
