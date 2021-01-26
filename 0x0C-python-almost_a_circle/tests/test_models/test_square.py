#!/usr/bin/python3
""" Test cases for square """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    """ Tests """

    def test_values(self):
        """ Test values """
        s = Square(27, 11, 0, 0)
        self.assertEqual(s.width, 27)
        self.assertEqual(s.height, 27)
        self.assertEqual(s.x, 11)
        self.assertEqual(s.y, 0)

        s = Square(50, 21, 3, 8)
        self.assertEqual(s.width, 50)
        self.assertEqual(s.height, 50)
        self.assertEqual(s.x, 21)
        self.assertEqual(s.y, 3)

    def test_errors(self):
        """ Test errors """
        s = (3, 4, '6', 9)
        self.assertRaises(TypeError, Square, s)

        s = (3, (4), 6, 9)
        self.assertRaises(TypeError, Square, s)

        s = ([3], 4, '6', 9)
        self.assertRaises(TypeError, Square, s)

        s = ((3), [4], 6, 9)
        self.assertRaises(TypeError, Square, s)

    def test_non_values(self):
        """ Test invalid values """
        s = [0, 2, 3, 4]
        self.assertRaises(ValueError, Square, *s)

        s = [-1, 2, 3, 4]
        self.assertRaises(ValueError, Square, *s)

        s = [-1, 0, 3, 4]
        self.assertRaises(ValueError, Square, *s)

        s = [1, -2, 3, -4]
        self.assertRaises(ValueError, Square, *s)

    def test_area(self):
        """ Area tests """
        s1 = Square(5, 4)
        self.assertEqual(s1.area(), 25)
        self.assertNotEqual(s1.area(), 20)

        s2 = Square(10, 5)
        self.assertEqual(s2.area(), 100)
        self.assertNotEqual(s2.area(), 50)

        s3 = Square(3, 4, 9, 44)
        self.assertEqual(s3.area(), 9)
        self.assertNotEqual(s3.area(), 108)

    def test_args(self):
        """ Args update test """
        s1 = Square(3, 2)
        args = [20, '9', 7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [(20), 9, 7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [20, 9, [7], 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [20, -9, 7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [-20, 9, 7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [-20, -9, 7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        args = [20, 9, -7, 0, 2]
        self.assertRaises(TypeError, s1.update(args))

        s1 = Square(2, 4, 6, 8)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 6)
        s1.update(1, 3, 5, 7)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 7)
        s1.update(102, 103)
        self.assertEqual(s1.width, 103)
        self.assertEqual(s1.height, 103)

    def test_kwargs(self):
        """ Test kwargs update """
        s1 = Square(20, 12)

        kwargs = {'id': 400, 'width': 10, 'height': '19', 'x': 0, 'y': 0}
        self.assertRaises(TypeError, s1.update(kwargs))

        kwargs = {'id': 400, 'width': (10), 'height': 19, 'x': 0, 'y': 0}
        self.assertRaises(TypeError, s1.update(kwargs))

        kwargs = {'id': 400, 'width': [10], 'height': (19), 'x': 0, 'y': 0}
        self.assertRaises(TypeError, s1.update(kwargs))

        kwargs = {'id': 400, 'width': 10, 'height': 19, 'x': 3, 'y': (3)}
        self.assertRaises(TypeError, s1.update(kwargs))

        kwargs = {'id': 400, 'width': 10, 'height': 19, 'x': [3], 'y': 3}
        self.assertRaises(TypeError, s1.update(kwargs))

        kwargs = {'id': 300, 'width': -10, 'height': 19, 'x': 3, 'y': 3}
        self.assertRaises(ValueError, s1.update(kwargs))

        kwargs = {'id': 300, 'width': 10, 'height': 19, 'x': 3, 'y': -3}
        self.assertRaises(ValueError, s1.update(kwargs))

        kwargs = {'id': 345, 'width': 10, 'height': -19, 'x': -3, 'y': 3}
        self.assertRaises(ValueError, s1.update(kwargs))

        s1 = Square(11, 5, 9, 8)
        self.assertEqual(s1.width, 11)
        self.assertEqual(s1.height, 11)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 9)
        self.assertEqual(s1.id, 8)


if __name__ == "__main__":
    unittest.main()
