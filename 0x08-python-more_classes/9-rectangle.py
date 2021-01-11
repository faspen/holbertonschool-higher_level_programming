#!/usr/bin/python3
"""Module containing rectangle class"""


class Rectangle:

    """Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ constructor for class
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """height getter
        return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter
        return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """area method
        return: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter method
        return: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """return printable representation
        """
        string = ""
        if self.__width > 0 and self.__height > 0:
            for item in range(self.__height):
                string += str(self.print_symbol) * self.__width
                string += "\n"
            string = string[:-1]
        return string

    def __repr__(self):
        """return actual string
        """
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'

    def __del__(self):
        """Delete rectangle
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return rectangle with dimensions equal to size
        """
        return cls(size, size)
