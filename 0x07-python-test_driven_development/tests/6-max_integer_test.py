#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ Tests in class
    """

    def maxint_tests(self):
        self.assertEqual(max_integer([1, 2, 3, 44, 5]), 44)
        self.assertEqual(max_integer([-34, -23, -2, 5]), 5)
        self.assertEqual(max_integer([-3, -4, -5, -6, -7]), -3)
        self.assertEqual(
            max_integer([2.34, 4.21, 55.6, float(7)]), float(55.6))
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1.0, 1.1, 1.3, 1.2]), 1.3)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-32.5, -4.1]), -4.1)
        self.assertEqual(max_integer([1.2, 3 / 2, 1.3]), 3 / 2)
