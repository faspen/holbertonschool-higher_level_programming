#!/usr/bin/python3
""" Module with from_json_string function """
import json


def from_json_string(my_str):
    """ return object from json format
    """
    return json.loads(my_str)
