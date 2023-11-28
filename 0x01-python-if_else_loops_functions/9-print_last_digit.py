#!/usr/bin/python3
# 9-print_last_digit.py

"""Print the last digit of a number"""


def print_last_digit(number):
    if number < 0:
        number *= -1
    n = number % 10
    print(f"{n}", end="")
    return n
