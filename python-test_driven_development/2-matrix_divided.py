#!/usr/bin/python3
"""
Module Name: 2-matrix_divided
Description: Divides all elements of a matrix
Authors: Lusanco, Ltoro9, Antoniofdjs Date: Feb 01 2024
"""


def matrix_divided(matrix, div):
    """Description: Divides all elements of a matrix
    - matrix (list): 2d array.
    - div (int or float): Number to divide by."""

    mtx = "matrix must be a matrix (list of lists) of integers/floats"
    siz = "Each row of the matrix must have the same size"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    temp = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(mtx)
        if temp != len(row):
            raise TypeError(siz)
        temp = len(row)

    new_matrix = [row[:] for row in matrix]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not isinstance(matrix[row][column], (int, float)):
                raise TypeError(mtx)
            result = round(matrix[row][column] / div, 2)
            new_matrix[row][column] = result

    return new_matrix