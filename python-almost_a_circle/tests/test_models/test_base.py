#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """Testing id when __init__ is used"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(3)
        self.assertEqual(b2.id, 3)
        b3 = Base(-2)
        self.assertEqual(b3.id, -2)


if __name__ == '__main__':

    unittest.main()
