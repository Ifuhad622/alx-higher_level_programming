#!/usr/bin/python3
# 12-fizzbuzz.py

"""Prints the numbers from 1 to 100"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{i}", end=" ")
