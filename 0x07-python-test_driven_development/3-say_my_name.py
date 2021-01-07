#!/usr/bin/python3
""" Module with say_my_name function """


def say_my_name(first_name, last_name=""):
    """ Print first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return (print("My name is {} {}\n".format(first_name, last_name), end=''))
