#!/usr/bin/python3
"""Module with peak funtion"""


def find_peak(list_of_integers):
    """Find peak"""
    if not list_of_integers:
        return None
    j = list_of_integers[0]
    for i in list_of_integers:
        if j < i:
            j = i
    return j
