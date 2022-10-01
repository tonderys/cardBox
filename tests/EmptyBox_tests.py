import unittest
import sys

sys.path.append("..")

from EmptyBox import *
from PrinterConstants import *

_ = 1
walls = 2 * min_wall_thickness

class EmptyBox_tests(unittest.TestCase):
    def test_get_wall_of_unmodified_box_should_return_minimal_wall_thickness(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.get_wall_x(), min_wall_thickness)
        self.assertEqual(sut.get_wall_y(), min_wall_thickness)
        self.assertEqual(sut.get_wall_z(), min_wall_thickness)

    def test_get_wall_x_of_modified_box_should_return_minimal_wall_thickness_increased_by_delta(self):
        sut = EmptyBox(Cube(_, _, _))
        sut.increase_width(5)
        self.assertEqual(sut.get_wall_x(), min_wall_thickness + (5/2))

    def test_get_wall_y_of_modified_box_should_return_minimal_wall_thickness_increased_by_delta(self):
        sut = EmptyBox(Cube(_, _, _))
        sut.increase_height(7)
        self.assertEqual(sut.get_wall_y(), min_wall_thickness + (7/2))

    def test_get_wall_z_of_modified_box_should_return_minimal_wall_thickness_increased_by_delta(self):
        sut = EmptyBox(Cube(_, _, _))
        sut.increase_depth(4)
        self.assertEqual(sut.get_wall_z(), min_wall_thickness + (4/2))

    def test_basic_empty_box_has_outer_diameters_enlarged_by_minimal_wall_thickness_on_each_side(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.outer.width, 10 + walls)
        self.assertEqual(sut.outer.height, 20 + walls)
        self.assertEqual(sut.outer.depth, 30 + walls)

    def test_basic_empty_box_has_inner_diameters_as_requested(self):
        sut = EmptyBox(Cube(10, 20, 30))
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.inner.depth, 30)

    def test_increasing_width_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(10, _, _))
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.outer.width, 10 + walls)
        sut.increase_width(3)
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.outer.width, 10 + walls + 3)

    def test_increasing_height_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(_, 20, _))
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.outer.height, 20 + walls)
        sut.increase_height(7)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.outer.height, 20 + walls + 7)

    def test_increasing_depth_changes_only_outer_diameter(self):
        sut = EmptyBox(Cube(_, _, 30))
        self.assertEqual(sut.inner.depth, 30)
        self.assertEqual(sut.outer.depth, 30 + walls)
        sut.increase_depth(5)
        self.assertEqual(sut.inner.depth, 30)
        self.assertEqual(sut.outer.depth, 30 + walls + 5)

if __name__ == '__main__':
    unittest.main()