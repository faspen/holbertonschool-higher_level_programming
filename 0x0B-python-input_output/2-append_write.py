#!/usr/bin/python3
""" Module with append_write fucntion """


def append_write(filename="", text=""):
    """ Add text to a file
    """
    with open(filename, encoding='utf-8', mode='a') as data:
        return data.write(text)
