import unittest
import sys

sys.path.append("..")

from WithJoints import WithJoints
from EmptyBox import EmptyBox

class WithJoints_tests(unittest.TestCase):
    def test_enlarging_the_box_to_a_minimum_value(self):
        box = EmptyBox(1,1,1);
        with_joints = WithJoints(box)
        assert(with_joints.box.outer.width == 7.5)
        assert(with_joints.box.outer.height == 7.5)

    def test_enlarging_the_box_to_46x60(self):
        box = EmptyBox(45,59,1);
        with_joints = WithJoints(box)
        assert(with_joints.box.outer.width == 52.5)
        assert(with_joints.box.outer.height == 61.5)

    def test_enlarging_the_box_to_46x60(self):
        box = EmptyBox(46,60,1);
        with_joints = WithJoints(box)
        assert(with_joints.box.outer.width == 52.5)
        assert(with_joints.box.outer.height == 70.5)