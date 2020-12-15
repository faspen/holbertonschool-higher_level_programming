#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for i in matrix:
        for j in i:
            if (idx == 0):
                print("{:d}".format(j), end='')
            else:
                print("{:2d}".format(j), end='')
            idx += 1
        idx = 0
        print()
