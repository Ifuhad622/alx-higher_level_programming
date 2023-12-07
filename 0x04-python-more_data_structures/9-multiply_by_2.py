#!/usr/bin/python3
# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """Return new dictionary with all values multiplied by 2."""
    dict_new = a_dictionary.copy()
    list_keys = list(dict_new.keys())

    for item in list_keys:
        dict_new[item] *= 2

    return (dict_new)
