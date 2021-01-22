#!/usr/bin/python3
""" Module containing rectangle class """
from base import Base


class Rectangle(Base):

    """ Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Get area
        """
        return self.__height * self.__width

    def display(self):
        """Print rectangle"""
        print("\n" * self.y, end='')
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """ Return printable representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign arguments"""
        for i in range(len(args)):
            if i == 0:
                super().__init__(args[0])
            if i == 1:
                self.width = args[1]
            if i == 2:
                self.height = args[2]
            if i == 3:
                self.x = args[3]
            if i == 4:
                self.y = args[4]

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """ Return dict """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
