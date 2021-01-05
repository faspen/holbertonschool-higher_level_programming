#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size is not 0:
            for a in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
