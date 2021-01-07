#!/usr/bin/python3
""" This module has the matrix_divided function """


def matrix_divided(matrix, div):
    """ Divide a matrix by div
    """
    errT = "matrix must be a matrix (list of lists) of integers/floats"
    errR = "Each row of the matrix must have the same size"
    new_list = []
    if matrix is None:
        raise TypeError(errT)
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                rowlen = len(matrix[0])
                if len(row) != rowlen:
                    raise TypeError(errR)
                else:
                    for i in row:
                        if not isinstance(i, int) and not isinstance(i, float):
                            raise TypeError(errT)
                    new_list.append(
                        list(map(lambda x: round(x / div, 2), row)))
            else:
                raise TypeError(errT)
    else:
        raise TypeError(errT)
    return new_list
