import unittest

from parametricBox.interior.Cube import *

from parametricBox.helpers.Notch import *

from parametricBox.WithJoints import *
from parametricBox.PlainBox import *

_ = 1

class WithJoints_tests(unittest.TestCase):
    def setUp(self):
        self.notch = Notch(_)
        self.both_sides_notch_height = 2 * self.notch.h
        self.minimal_case = self.notch.a + self.notch.b - self.notch.delta
        self.minimal_dimension = self.minimal_case + self.both_sides_notch_height

        self.minimal_walls = min_wall_thickness * 2

    def test_enlarging_the_box_to_a_minimum_value(self):
        box = PlainBox(Cube(1,1,1))
        sut = WithJoints(box)
        self.assertEqual(sut.get_width(), self.minimal_dimension)
        self.assertEqual(sut.get_height(), self.minimal_dimension)

    def test_ideal_minimal_box_without_enlarging(self):
        max_input_dimension = self.minimal_case - self.minimal_walls

        self.assertEqual(max_input_dimension, 3.5)
        self.assertEqual(self.minimal_dimension, 10.5)

        sut = WithJoints(PlainBox(Cube(max_input_dimension, max_input_dimension, _)))
        self.assertEqual(sut.get_width(), self.minimal_dimension)
        self.assertEqual(sut.get_height(), self.minimal_dimension)

    def test_not_enlarging_big_box(self):
        width = 36 - self.minimal_walls - self.notch.delta
        height = 45 - self.minimal_walls - self.notch.delta

        self.assertEqual(width, 30.5)
        self.assertEqual(height, 39.5)

        sut = WithJoints(PlainBox(Cube(width,height,_)))
        self.assertEqual(sut.get_width(),  37.5)
        self.assertEqual(sut.get_height(), 46.5)

    def test_enlarging_big_box(self):
        sut = WithJoints(PlainBox(Cube(31,40,_)))
        self.assertEqual(sut.get_width(),  46.5)
        self.assertEqual(sut.get_height(), 55.5)
