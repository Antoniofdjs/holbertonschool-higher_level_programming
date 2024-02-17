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

    def test_save_to_file(self):
        """Save json string into file, list of dictionaries"""
        # Rectangle Test
        expected_list_of_dic = [
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
            {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
            ]
        json_expeceted = Rectangle.to_json_string(expected_list_of_dic)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), json_expeceted)

        # Square Test, creations above count for ids below
        expected_list_of_dic = [
            {'id': 3, 'size': 10, 'x': 7, 'y': 2},
            {'id': 4, 'size': 2, 'x': 0, 'y': 0}
            ]
        json_expeceted = Square.to_json_string(expected_list_of_dic)
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json") as f:
            self.assertEqual(f.read(), json_expeceted)


if __name__ == '__main__':

    unittest.main()
