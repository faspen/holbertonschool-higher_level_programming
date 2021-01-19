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
        if type(value) != int:
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
