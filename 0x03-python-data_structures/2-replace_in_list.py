#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replace element in list at specific position"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)
