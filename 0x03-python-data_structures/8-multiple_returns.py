#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Return tuple with string length and first character"""
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)
