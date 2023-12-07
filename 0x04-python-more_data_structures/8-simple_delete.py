#!/usr/bin/python3
# 8-simple_delete.py


def simple_delete(a_dictionary, key=""):
    """Delete key in a dictionary."""
    a_dictionary.pop(key, None)
    return (a_dictionary)
