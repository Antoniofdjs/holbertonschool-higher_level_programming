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
        """test init for Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(TypeError, Rectangle, 0)
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, 1, -2)

    def test_validator_types(self):
        """Validate that types must be int, except id"""
        # Testing creator
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(TypeError, Rectangle, 1, [34])
        self.assertRaises(TypeError, Rectangle, 1, 2, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        # Testing setters
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.width = "-2"
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.height = "0"
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.x = [-1]
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.y = (-1, 4)

    def test_validator_values(self):
        """Validate values (except id), and w,h >0 and x,y >=0"""
        # Testing constructor
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        # Testing setters
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.width = -2
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.height = 0
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.x = -1
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            r1.y = -1

    def test_area(self):
        """test .area, returns area of rectangle"""
        r10 = Rectangle(3, 2)
        self.assertEqual(r10.area(), 6)
        r11 = Rectangle(2, 10)
        self.assertEqual(r11.area(), 20)
        r12 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r12.area(), 56)

    def test_str_representation(self):
        """ Represents [Rectangle] (id) x/y - w/h"""
        r1 = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 3/4 - 1/2")

    def test_update(self):
        """ order of udpate is id, width, height, x, y"""
        r1 = Rectangle(5, 2, 6, 7)
        r1.update(height=1, id=5)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 6/7 - 5/1")
        r2 = Rectangle(1, 5, 3, 3, 10)
        r2.update(15, 10, id=5)
        self.assertEqual(r2.__str__(), "[Rectangle] (15) 3/3 - 10/5")
        r3 = Rectangle(1, 3)
        r3.update(id=3, x=4, y=4, width=2, height=3)
        self.assertEqual(r3.__str__(), "[Rectangle] (3) 4/4 - 2/3")


if __name__ == "__main__":

    unittest.main()
