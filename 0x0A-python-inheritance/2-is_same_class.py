#!/usr/bin/python3
""" Module with is_same_class function """


def is_same_class(obj, a_class):
    """
    Return true if obj is the
    same as a_class. Otherwise
    false
    """
    return True if isinstance(obj, a_class) else False
