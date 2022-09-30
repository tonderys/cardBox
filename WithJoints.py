from numpy import arange
import solid
from solid.utils import *

from Notch import Notch

class WithJoints:
    def __init__(self, box):
        self.box = box
        self.notch = Notch(self.box.outer.depth)
        self._adjust_walls()
        self.joints = [self._get_upper_joints(), self._get_right_joints(),
                       self._get_lower_joints(), self._get_left_joints()]

    def _get_joints(self, length):
        assert((length + self.notch.delta) % self.notch.get_interlocked_length() == 0)
        joint = self.notch.scad()
        joints = union()([solid.translate([i, 0, 0])(joint) for i in arange(0,length, self.notch.get_interlocked_length())])
        return intersection()(cube([length, self.notch.h, self.notch.height]), joints)

    def _get_upper_joints(self):
        joints = self._get_joints(self.box.outer.width)
        return forward(self.box.outer.height)(joints)

    def _get_right_joints(self):
        joints = self._get_joints(self.box.outer.height)
        joints = rotate([0, 0, -90])(joints)
        return translate([self.box.outer.width, self.box.outer.height, 0])(joints)

    def _get_lower_joints(self):
        joints = self._get_joints(self.box.outer.width)
        joints = rotate([0, 0, 180])(joints)
        return right(self.box.outer.width)(joints)

    def _get_left_joints(self):
        joints = self._get_joints(self.box.outer.height)
        return rotate([0, 0, 90])(joints)

    def _get_delta(self, length):
        mod = length % self.notch.get_interlocked_length()
        if mod == self.notch.get_interlocked_length() - self.notch.delta: return 0
        delta = self.notch.get_interlocked_length() - mod - self.notch.delta
        return delta if delta > 0 else delta + self.notch.get_interlocked_length()

    def _adjust_walls(self):
        self.box.increase_width(self._get_delta(self.box.outer.width))
        self.box.increase_height(self._get_delta(self.box.outer.height))

    def scad(self):
        return solid.union()(self.box.scad(), self.joints)
