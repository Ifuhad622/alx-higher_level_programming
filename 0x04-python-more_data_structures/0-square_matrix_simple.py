#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """Compute square value of all integers in matrix."""
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
