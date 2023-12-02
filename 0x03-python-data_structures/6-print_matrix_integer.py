#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """Print matrix of integers"""
    for i_row in matrix:
        for i_col in i_row:
            print("{:d}".format(i_col), end=" " if i_col != i_row[-1] else "")
        print()
