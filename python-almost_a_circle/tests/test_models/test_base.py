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


    def test_save_to_file_none(self):
        """Test case for save_to_file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    def test_create_rectangle(self):
        """Test for using create, Rectangle"""
        r1 = Rectangle(3, 5, 1, 1)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """Test using create, Square"""
        sqr1 = Square(5)
        dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**dictionary)
        self.assertEqual(sqr1 == sqr2, False)
        self.assertEqual(sqr1 is sqr2, False)
        self.assertNotEqual(sqr1, sqr2)

    def test_save_to_file(self):
        """Test case for save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), '[]')


if __name__ == '__main__':

    unittest.main()
