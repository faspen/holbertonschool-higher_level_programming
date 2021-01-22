#!/usr/bin/python3
""" Module with Base class """
import json


class Base():

    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class initializer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json string to a file """
        list = []
        fil = cls.__name__ + '.json'
        if list_objs is not None:
            for item in list_objs:
                list.append(item.to_dictionary())
        with open(fil, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list))
