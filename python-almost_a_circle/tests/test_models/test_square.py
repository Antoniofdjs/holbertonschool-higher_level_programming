#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
        Rectangle __init__(width,height,x=0,y=0,id=none)
    """

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_init_rectangle(self):
        """Test creation for square (size, x=0, y=0, id=None)"""
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s2.id, 4)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_validator_types(self):
        """Validate that types must be int, except id"""
        # Testing creator
        self.assertRaises(TypeError, Square, "10", 2)
        self.assertRaises(TypeError, Square, 1, [34])
        self.assertRaises(TypeError, Square, 1, 2, "4")
        # Testing setters
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.size = "-2"
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.x = "-2"
        with self.assertRaises(TypeError):
            s1 = Square(1)
            s1.y = "-2"


if __name__ == "__main__":

    unittest.main()
