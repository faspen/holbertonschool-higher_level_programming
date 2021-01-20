#!/usr/bin/python3
""" Module with save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """ Write json text into file
    """
    with open(filename, encoding='utf-8', mode='w') as j:
        json.dump(my_obj, j)
