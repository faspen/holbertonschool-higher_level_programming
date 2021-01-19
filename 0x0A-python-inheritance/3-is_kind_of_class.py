#!/usr/bin/python3
""" Module with is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """
    Return True if obj comes from
    a_class
    """
    return True if isinstance(obj, a_class) else False
