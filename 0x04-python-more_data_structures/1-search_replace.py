#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """Replaces all occurrences of element by another in new list"""
    list_new = list(map(lambda x: replace if x == search else x, my_list))
    return (list_new)
