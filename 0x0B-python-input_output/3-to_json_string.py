#!/usr/bin/python3
""" Module with to_json_string fucntion """
import json


def to_json_string(my_obj):
    """ Return JSON version of string
    """
    return json.dumps(my_obj)
