#!/usr/bin/python3
# 101-remove_char_at.py

"""Create copy of string, remove character at the position n"""


def remove_char_at(str, n):
    strcpy = ""
    for i in range(len(str)):
        if i != n:
            strcpy += str[i]
    return (strcpy)
