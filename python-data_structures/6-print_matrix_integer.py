#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in range(0, len(row)):
            if column == len(row) - 1:
                print('{:d}'.format(row[column]), end='')
            else:
                print('{:d}'.format(row[column]), end=' ')
        print()
