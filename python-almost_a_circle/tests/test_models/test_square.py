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

        self.assertRaises(ValueError, Square, 0)

    def test_validator_types(self):
        """Validate that types must be int, except id
            (size, x=0, y=0, id=None)
        """
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

    def test_validator_values(self):
        """Validate that size > 0, x and y >= 0
            (size, x=0, y=0, id=None)
        """
        # Testing creator
        self.assertRaises(ValueError, Square, -3, 2)
        self.assertRaises(ValueError, Square, 1, -34)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        # Testing setters
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.size = -2
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.x = -2
        with self.assertRaises(ValueError):
            s1 = Square(1)
            s1.y = -2

    def test_area(self):
        """test .area, returns area of square"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(4, 10)
        self.assertEqual(s2.area(), 16)
        s3 = Square(2, 7, 6, 10)
        self.assertEqual(s3.area(), 4)

    def test_str_representation(self):
        """ Square [Square] (id) x/y - size"""
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")

    def test_update(self):
        """ order of udpate is [id, width(size), x, y]
            update(self, *args, **kwargs)
        """
        # Testing **kwargs
        s1 = Square(1, 2, 3, 4)
        s1.update(id=10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")
        s2 = Square(1, 2, 3, 4)
        s2.update(id=10, size=10)
        self.assertEqual(s2.__str__(), "[Square] (10) 2/3 - 10")
        s3 = Square(1, 2, 3, 4)
        s3.update(id=10, size=10, x=10)
        self.assertEqual(s3.__str__(), "[Square] (10) 10/3 - 10")
        s4 = Square(1, 2, 3, 4)
        s4.update(id=10, size=10, x=10, y=10)
        self.assertEqual(s4.__str__(), "[Square] (10) 10/10 - 10")
        # Testing args
        s1 = Square(1, 2, 3, 4)
        s1.update(10, size=10, x=10, y=10)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/3 - 1")
        s2 = Square(1, 2, 3, 4)
        s2.update(10, 10, x=10, y=10)
        self.assertEqual(s2.__str__(), "[Square] (10) 2/3 - 10")
        s3 = Square(1, 2, 3, 4)
        s3.update(10, 10, 10, y=10)
        self.assertEqual(s3.__str__(), "[Square] (10) 10/3 - 10")
        s4 = Square(1, 2, 3, 4)
        s4.update(10, 10, 10, 10)
        self.assertEqual(s4.__str__(), "[Square] (10) 10/10 - 10")

    def test_to_dictionary(self):
        """returns dictionary represetantion of Square"""
        s1 = Square(10, 2, 1)
        expected_dictionary = {
            'id': 1,
            'size': 10,
            'x': 2,
            'y': 1
            }
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, expected_dictionary)

    def test_save_to_file(self):
        """Save json string into file, list of dictionaries"""
        expected_list_of_dic = [
            {'id': 1, 'size': 10, 'x': 7, 'y': 2},
            {'id': 2, 'size': 2, 'x': 0, 'y': 0}
            ]
        json_expeceted = Square.to_json_string(expected_list_of_dic)
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json") as f:
            self.assertEqual(f.read(), json_expeceted)

if __name__ == "__main__":

    unittest.main()
