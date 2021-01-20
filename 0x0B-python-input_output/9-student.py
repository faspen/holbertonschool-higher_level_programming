#!/usr/bin/python3
""" Module with student class """


class Student:

    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initialization for student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve dict of Student instance
        """
        return self.__dict__
