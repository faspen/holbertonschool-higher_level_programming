#!/usr/bin/python3
""" Module with load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Create object from json file
    """
    with open(filename, encoding='utf-8') as js:
        return json.load(js)
