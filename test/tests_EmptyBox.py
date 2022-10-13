import unittest
import sys

sys.path.append("..")

from EmptyBox import *
from PrinterConstants import *

_ = 1
walls = 2 * min_wall_thickness
floors = 2 * min_floor_thickness

class EmptyBox_tests(unittest.TestCase):
    def test_get_wall_of_unmodified_box_should_return_minimal_wall_thickness(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.get_wall_x(), min_wall_thickness)
        self.assertEqual(sut.get_wall_y(), min_wall_thickness)
        self.assertEqual(sut.get_wall_z(), min_floor_thickness)

    def test_basic_empty_box_has_outer_diameters_enlarged_by_minimal_wall_thickness_on_each_side(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.get_width(), 10 + walls)
        self.assertEqual(sut.get_height(), 20 + walls)
        self.assertEqual(sut.get_depth(), 30 + floors)

    def test_basic_empty_box_has_inner_diameters_as_requested(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.inner.depth, 30)

    def test_increasing_width_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(10, _, _))
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.get_width(), 10 + walls)
        sut.increase_width(3)
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.get_width(), 10 + walls + 3)

    def test_increasing_height_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(_, 20, _))
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.get_height(), 20 + walls)
        sut.increase_height(7)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.get_height(), 20 + walls + 7)

    def test_increasing_depth_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(_, _, 30))
        self.assertEqual(sut.inner.depth, 30)
        self.assertEqual(sut.get_depth(), 30 + floors)
        sut.increase_depth(5)
        self.assertEqual(sut.inner.depth, 30)
        self.assertEqual(sut.get_depth(), 30 + floors + 5)

if __name__ == '__main__':
    unittest.main()