#!/usr/bin/python3
"""This module validates a square's size"""


class Square:

    """ Square class """

    def __init__(self, size=0):
        """__init__ constructor for square class

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be and integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
