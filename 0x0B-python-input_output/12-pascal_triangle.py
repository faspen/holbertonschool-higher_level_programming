#!/usr/bin/python3
""" Module containing pascal_triangle function """
import math


def pascal_triangle(n):
    """ Print pascal triangle
    """
    if n <= 0:
        return []
    lis = [1]
    for i in range(n):
        print(lis)
        newlist = []
        newlist.append(lis[0])
        for j in range(len(lis) - 1):
            newlist.append(lis[j] + lis[j + 1])
        newlist.append(lis[-1])
        lis = newlist
    return lis
