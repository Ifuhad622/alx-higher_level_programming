#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers on list in reverse order."""
    if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
