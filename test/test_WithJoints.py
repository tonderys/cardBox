import unittest
import sys

sys.path.append("..")

from WithJoints import *
from EmptyBox import *
from Cube import *

class WithJoints_tests(unittest.TestCase):
    def test_enlarging_the_box_to_a_minimum_value(self):
        box = EmptyBox(Cube(1,1,1))
        with_joints = WithJoints(box)
        assert(with_joints.box.get_width() == 7.5)
        assert(with_joints.box.get_height() == 7.5)

    def test_enlarging_the_box_to_45x59(self):
        box = EmptyBox(Cube(45,59,1))
        with_joints = WithJoints(box)
        assert(with_joints.box.get_width() == 52.5)
        assert(with_joints.box.get_height() == 61.5)

    def test_enlarging_the_box_to_46x60(self):
        box = EmptyBox(Cube(46,60,1))
        with_joints = WithJoints(box)
        assert(with_joints.box.get_width() == 52.5)
        assert(with_joints.box.get_height() == 70.5)