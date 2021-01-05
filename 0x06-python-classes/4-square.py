#!/usr/bin/python3
"""This module introduces getter and setter"""


class Square:

    """ Square class """

    def __init__(self, size=0):
        """__init__ constructor for square class

        Args:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        """ get area of Square
        return: area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ size getter
        return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter

        Args:
            value (int): given value
        return: size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
