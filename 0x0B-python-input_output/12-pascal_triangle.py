#!/usr/bin/python3
""" Module containing pascal_triangle function """
import math


def pascal_triangle(n):
    """ Print pascal triangle
    """
    if n <= 0:
        return []

    result = []
    for count in range(n):
        tmp = []
        for element in range(count + 1):
            tmp.append(combination(count, element))
        result.append(tmp)
    return result


def combination(n, r):
    """ Helper function
    """
    return int((math.factorial(n)) / ((math.factorial(r)) *
                                      math.factorial(n - r)))
