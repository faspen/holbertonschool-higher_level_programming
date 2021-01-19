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
