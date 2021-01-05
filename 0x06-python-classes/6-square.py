#!/usr/bin/python3
class Square:

    """ Square class """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ constructor for square class

        Args:
            size (int): size of square
            position (tuple): coordinates
        """
        self.position = size
        self.size = size

    def area(self):
        """ get area
        return: area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ size getter
        return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter

        Args:
            value (int): given value
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ position getter
        return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter

        Args:
            value (int): given value
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ print square """
        if self.__size is not 0:
            if self.__position[1] is not 0:
                print("\n" * self.__position[1], end='')
            else:
                print("{}".format(" " * self.__position[0]), end='')
                print("{}".format("#" * self.__size))
        else:
            print("")
