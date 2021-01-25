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

    def test_args(self):
        """ Test args update """
        r1 = Rectangle(3, 2)
        args = [20, '9', 7, 0, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [(20), 9, 7, 0, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [20, 9, [7], 0, 2]
        self.assertRaises(TypeError, r1.update(args))

        args = [20, -9, 7, 0, 2]
        self.assertRaises(ValueError, r1.update(args))

        args = [-20, 9, 7, 0, 2]
        self.assertRaises(ValueError, r1.update(args))

        args = [-20, -9, 7, 0, 2]
        self.assertRaises(ValueError, r1.update(args))

        args = [20, 9, -7, 0, 2]
        self.assertRaises(ValueError, r1.update(args))

        r1 = Rectangle(2, 4, 6, 8)
        r1.update(100, 1, 3, 5, 7)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)
        r1.update(102)
        self.assertEqual(r1.id, 102)

    def test_kwargs(self):
        """ Test kwargs update """
        r1 = Rectangle(20, 12)

        kwargs = {'id': 400, 'width': 10, 'height': '19', 'x': 0, 'y': 0}
        self.assertRaises(TypeError, r1.update(kwargs))

        kwargs = {'id': 400, 'width': (10), 'height': 19, 'x': 0, 'y': 0}
        self.assertRaises(TypeError, r1.update(kwargs))

        kwargs = {'id': 400, 'width': [10], 'height': (19), 'x': 0, 'y': 0}
        self.assertRaises(TypeError, r1.update(kwargs))

        kwargs = {'id': 400, 'width': 10, 'height': 19, 'x': 3, 'y': (3)}
        self.assertRaises(TypeError, r1.update(kwargs))

        kwargs = {'id': 400, 'width': 10, 'height': 19, 'x': [3], 'y': 3}
        self.assertRaises(TypeError, r1.update(kwargs))

        kwargs = {'id': 300, 'width': -10, 'height': 19, 'x': 3, 'y': 3}
        self.assertRaises(ValueError, r1.update(kwargs))

        kwargs = {'id': 300, 'width': 10, 'height': 19, 'x': 3, 'y': -3}
        self.assertRaises(ValueError, r1.update(kwargs))

        kwargs = {'id': 345, 'width': 10, 'height': -19, 'x': -3, 'y': 3}
        self.assertRaises(ValueError, r1.update(kwargs))

        r1 = Rectangle(30, 12, 4, 5)
        r1.update(id=89, width=15, height=6, x=2, y=3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        r1.update(id=92)
        self.assertEqual(r1.id, 92)


if __name__ == "__main__":
    unittest.main()
