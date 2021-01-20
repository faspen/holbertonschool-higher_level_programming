#!/usr/bin/python3
""" Module containing read_file function """


def read_file(filename=""):
    """ Read file and print to stdout
    """
    with open(filename, encoding='utf-8') as fi:
        info = fi.read()
        print(info, end="")
