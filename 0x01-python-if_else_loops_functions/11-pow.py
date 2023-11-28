#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print ASCII alphabet, in reverse order, lowercase and uppercase"""


for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2:
        i -= 32
    print("{:c}".format(i), end="")
    if i % 2:
        i += 32
