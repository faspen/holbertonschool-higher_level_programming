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

    def to_json(self, attrs=None):
        """ Retrieve dict of Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for names in attrs:
                for i in self.__dict__:
                    if i == names:
                        new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """ Replace all attributes of Student instance
        """
        if len(json) > 0:
            for i in json:
                self.__dict__[i] = json[i]
