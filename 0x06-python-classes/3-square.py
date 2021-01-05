#!/usr/bin/python3
"""This module finds the area of a square"""


class Square:

    """ Square class """

    def __init__(self, size=0):
        """__init__ constructor for Square class

        Args:
            size (int): size of Square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ get area of Square
        return: area
        """
        return (self.__size * self.__size)
