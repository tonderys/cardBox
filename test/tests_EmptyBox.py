import unittest
import sys

sys.path.append("..")

from parametricBox.PlainBox import *
from parametricBox.helpers.PrinterConstants import *

_ = 1
walls = 2 * min_wall_thickness
floors = 2 * min_floor_thickness

class EmptyBox_tests(unittest.TestCase):
    def test_get_wall_of_unmodified_box_should_return_minimal_wall_thickness(self):
        sut = PlainBox(Cube(10, 20, 30))
        self.assertEqual(sut.get_wall_x(), min_wall_thickness)
        self.assertEqual(sut.get_wall_y(), min_wall_thickness)
        self.assertEqual(sut.get_floor(), min_floor_thickness)

    def test_basic_empty_box_has_outer_diameters_enlarged_by_minimal_wall_thickness_on_each_side(self):
        sut = PlainBox(Cube(10, 20, 30))
        self.assertEqual(sut.width, 10 + walls)
        self.assertEqual(sut.height, 20 + walls)
        self.assertEqual(sut.depth, 30 + floors)

    def test_basic_empty_box_has_inner_diameters_as_requested(self):
        sut = PlainBox(Cube(10, 20, 30))
        self.assertEqual(sut.box.width, 10)
        self.assertEqual(sut.box.height, 20)
        self.assertEqual(sut.box.depth, 30)

if __name__ == '__main__':
    unittest.main()