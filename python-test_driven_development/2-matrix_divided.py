#!/usr/bin/python3
"""
Module Name: 2-matrix_divided
Description: Divides all elements of a matrix
Authors: Lusanco, Ltoro9, Antoniofdjs, Livanhernandez Date: Feb 01 2024
"""


def matrix_divided(matrix, div):
    """Description: Divides all elements of a matrix
    - matrix (list): 2d array.
    - div (int or float): Number to divide by."""

    mtx = "matrix must be a matrix (list of lists) of integers/floats"
    siz = "Each row of the matrix must have the same size"
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(siz)
        inner = []
        for elem in lists:
            if not isinstance(elem, (int, float)):
                raise TypeError(mtx)
            else:
                inner.append(round(elem / div, 2))
        result.append(inner)

    return result
