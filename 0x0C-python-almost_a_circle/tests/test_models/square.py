#!/usr/bin/python3
""" Module containing square class """
from models.rectangle import Rectangle


class Square(Rectangle):

    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Square initializer """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Return size """
        return super().width

    @size.setter
    def size(self, value):
        """ Set size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Update values """
        mylist = ["id", "size", "x", "y"]
        for num, val in enumerate(args):
            setattr(self, mylist[num], val)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """ Return dictionary """
        return {"x": self.x, "y": self.y, "size": self.size, "id": self.id}
