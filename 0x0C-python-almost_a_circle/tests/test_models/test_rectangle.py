#!/usr/bin/python3
""" Test cases for rectangle """
import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ Tests """

    def test_id(self):
        """id tests"""
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(44, 33)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 2, 3, 4, 50)
        self.assertEqual(r3.id, 50)
        r4 = Rectangle(4, 3, 2, 1, -4)
        self.assertEqual(r4.id, -4)

if __name__ == "__main__":
    unittest.main()
