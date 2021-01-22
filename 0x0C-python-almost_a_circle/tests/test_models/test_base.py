#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from base import Base


class TestBase(unittest.TestCase):

    def test_base(self):
        """tests"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(32)
        self.assertEqual(c.id, 32)

if __name__ == "__main__":
    unittest.main()
