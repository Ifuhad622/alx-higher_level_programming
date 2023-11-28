#!/usr/bin/python3
# 6-print_comb3.py

"""Prints all possible different combinations of two digits"""
n = 0
for i in range(10):
    j = 1 + n
    while j < 10:
        print("{}{}".format(i, j), end="")
        if i == 8 and j == 9:
            break
        j += 1
        print(",", end=" ")
    n += 1
print("")
