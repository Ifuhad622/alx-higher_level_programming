#!/usr/bin/python3
# 4-print_hexa.py

"""Print numbers 0 to 98 in decimal and hexadecimal."""
i = 0
for i in range(0, 99):
    print("{} = {}".format(i, hex(i)))
