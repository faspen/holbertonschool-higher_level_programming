#!/usr/bin/python3
""" Module containing bg class """


class BaseGeometry:

    """ Geometry class
    """

    def area(self):
        """ incomplete area function
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ method for validating ints
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """ Subclass of BaseGeometry
    """

    def __init__(self, width, height):
        """ initialize width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return area
        """
        return self.__width * self.__height

    def __str__(self):
        """ Return info
        """
        info = '[Rectangle] ' \
            + str(self.__width) + '/' + str(self.__height)
        return info
