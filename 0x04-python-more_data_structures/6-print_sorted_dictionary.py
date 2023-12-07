#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Print dictionary by ordered keys."""
    ord_list = list(a_dictionary.keys())
    ord_list.sort()
    for item in ord_list:
        print("{}: {}".format(item, a_dictionary.get(item)))
