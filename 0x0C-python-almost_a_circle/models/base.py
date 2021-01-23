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

    @staticmethod
    def from_json_string(json_string):
        """ Return from json string """
        if json_string is None or len(json_string) == 0:
            return []
        list = json.loads(json_string)
        return list

    @classmethod
    def create(cls, **dictionary):
        """ Return instance with all attributes set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(5, 5)
        if cls.__name__ == 'Square':
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instances
        """
        fil = cls.__name__ + '.json'
        list = []
        try:
            with open(fil, encoding='utf-8', mode='r') as f:
                inst = Base.from_json_string(f.read())
                return [cls.create(**dictions) for dictions in inst]
        except IOError:
            return []
