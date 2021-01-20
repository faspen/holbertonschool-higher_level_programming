#!/usr/bin/python3
""" Module with write_file function"""


def write_file(filename="", text=""):
    """ Write text into file
    """
    with open(filename, encoding='utf-8', mode='w') as data:
        return data.write(text)
