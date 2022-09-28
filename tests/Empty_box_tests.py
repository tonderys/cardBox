import unittest
import sys

sys.path.append("..")

from Empty_box import Empty_box

class Empty_box_tests(unittest.TestCase):
    def test_basic_empty_box_has_outer_diameters_enlarged_by_minimal_wall_thickness_on_each_side(self):
        sut = Empty_box(10, 20, 30)
        self.assertEqual(sut.outer.width, 12)
        self.assertEqual(sut.outer.height, 22)
        self.assertEqual(sut.outer.depth, 32)

    def test_basic_empty_box_has_inner_diameters_as_requested_except_for_depth(self):
        sut = Empty_box(10, 20, 30)
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.inner.depth, 31)

    def test_increasing_width_changes_only_outer_diameter(self):
        sut = Empty_box(10, 20, 30)
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.outer.width, 12)
        sut.increase_width(3)
        self.assertEqual(sut.inner.width, 10)
        self.assertEqual(sut.outer.width, 15)

    def test_increasing_height_changes_only_outer_diameter(self):
        sut = Empty_box(10, 20, 30)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.outer.height, 22)
        sut.increase_height(7)
        self.assertEqual(sut.inner.height, 20)
        self.assertEqual(sut.outer.height, 29)

    def test_increasing_depth_changes_inner_and_outer_diameter(self):
        sut = Empty_box(10, 20, 30)
        self.assertEqual(sut.inner.depth, 31)
        self.assertEqual(sut.outer.depth, 32)
        sut.increase_depth(5)
        self.assertEqual(sut.inner.depth, 33.5)
        self.assertEqual(sut.outer.depth, 37)

if __name__ == '__main__':
    unittest.main()