#!/usr/bin/python3
"""Module containing rectangle class"""


class Rectangle:

    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        """__init__ constructor for class
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter
        return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter
        return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """area method
        return: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter method
        return: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """return printable representation
        """
        string = ""
        if self.__width > 0 and self.__height > 0:
            for item in range(self.__height):
                string += "#" * self.__width
                string += "\n"
            string = string[:-1]
        return string

    def __repr__(self):
        """return actual string
        """
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'
