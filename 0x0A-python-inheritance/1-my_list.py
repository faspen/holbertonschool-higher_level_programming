#!/usr/bin/python3
""" Module with MyList and print """


class MyList(list):

    """ class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))
