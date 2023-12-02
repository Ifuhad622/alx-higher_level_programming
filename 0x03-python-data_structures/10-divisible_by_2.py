#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 on list"""
    multiples_2 = []
    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            multiples_2.append(True)
        else:
            multiples_2.append(False)

    return (multiples_2)
