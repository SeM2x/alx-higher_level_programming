#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 98, 3]), 98)
        self.assertEqual(max_integer([98, 1, 3]), 98)
        self.assertEqual(max_integer([3, 1, 98]), 98)
        self.assertEqual(max_integer([-98, 1, 3]), 3)
        self.assertEqual(max_integer([-1, -2 , -3]), -1)
        self.assertEqual(max_integer([98]), 98)
        self.assertEqual(max_integer([]), None)
