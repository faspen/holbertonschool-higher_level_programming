#!/usr/bin/python3
""" Module containing inherits_from function """


def inherits_from(obj, a_class):
    """
    Return True if object is from
    a class that inherited from
    specified class
    """
    obt = type(obj)
    if issubclass(obt, a_class) and obt != a_class:
        return True
    else:
        return False
