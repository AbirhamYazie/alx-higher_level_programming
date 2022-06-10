#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    U_matrix = []
    for row in matrix:
        U_matrix.append(list(map(lambda e: e**2, row)))
    return (U_matrix)


