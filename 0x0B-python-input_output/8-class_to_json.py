#!/usr/bin/python3
""" Module with class_to_json function """


def class_to_json(obj):
    """ Return dict description for json
    """
    return obj.__dict__
