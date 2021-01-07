#!/usr/bin/python3
""" Module containing print_square function """


def print_square(size):
    """ Function prints a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
