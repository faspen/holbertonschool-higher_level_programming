#!/usr/bin/python3
""" Test cases for rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ Tests """

    def test_values(self):
        """ Test values """
        r = Rectangle(10, 7, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

        r = Rectangle(30, 40, 25, 100)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 25)
        self.assertEqual(r.y, 100)

    def test_errors(self):
        """ Test errors """
        r = (3, 4, '6', 9)
        self.assertRaises(TypeError, Rectangle, r)

        r = (3, (4), 6, 9)
        self.assertRaises(TypeError, Rectangle, r)

        r = ([3], 4, '6', 9)
        self.assertRaises(TypeError, Rectangle, r)

        r = ((3), [4], 6, 9)
        self.assertRaises(TypeError, Rectangle, r)

    def test_non_values(self):
        """ Test invalid values """
        r = [0, 2, 3, 4]
        self.assertRaises(ValueError, Rectangle, *r)

        r = [-1, 2, 3, 4]
        self.assertRaises(ValueError, Rectangle, *r)

        r = [-1, 0, 3, 4]
        self.assertRaises(ValueError, Rectangle, *r)

        r = [1, -2, 3, -4]
        self.assertRaises(ValueError, Rectangle, *r)

    def test_area(self):
        """ Test area """
        r1 = Rectangle(4, 4)
        self.assertEqual(r1.area(), 16)

        r2 = Rectangle(5, 2)
        self.assertEqual(r2.area(), 10)
        self.assertNotEqual(r2.area(), -10)

        r3 = Rectangle(6, 5, 0, 0, 3)
        self.assertEqual(r3.area(), 30)
        self.assertNotEqual(r3.area(), 90)


if __name__ == "__main__":
    unittest.main()
