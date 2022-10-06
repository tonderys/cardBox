from numpy import arange
from solid import *
from solid.utils import *

from Notch import *
from EmptyBox import *
from MeasuredObject import *

class WithJoints(MeasuredObject):
    def __init__(self, box: EmptyBox):
        self.box = box
        self._notch = Notch(self.box.get_depth())
        self._adjust_walls()
        self._joints = [self._get_upper_joints(), self._get_right_joints(),
                       self._get_lower_joints(), self._get_left_joints()]

    def _get_joints(self, length):
        assert((length + self._notch.delta) % self._notch.get_interlocked_length() == 0)
        joint = self._notch.scad()
        joints = union()([translate([i, 0, 0])(joint) for i in arange(0,length, self._notch.get_interlocked_length())])
        return intersection()(cube([length, self._notch.h, self._notch.height]), joints)

    def _get_upper_joints(self):
        joints = self._get_joints(self.box.get_width())
        return forward(self.box.get_height())(joints)

    def _get_right_joints(self):
        joints = self._get_joints(self.box.get_height())
        joints = rotate([0, 0, -90])(joints)
        return translate([self.box.get_width(), self.box.get_height(), 0])(joints)

    def _get_lower_joints(self):
        joints = self._get_joints(self.box.get_width())
        joints = rotate([0, 0, 180])(joints)
        return right(self.box.get_width())(joints)

    def _get_left_joints(self):
        joints = self._get_joints(self.box.get_height())
        return rotate([0, 0, 90])(joints)

    def _get_delta(self, length):
        mod = length % self._notch.get_interlocked_length()
        if mod == self._notch.get_interlocked_length() - self._notch.delta: return 0
        delta = self._notch.get_interlocked_length() - mod - self._notch.delta
        return delta if delta > 0 else delta + self._notch.get_interlocked_length()

    def _adjust_walls(self):
        self.box.increase_width(self._get_delta(self.box.get_width()))
        self.box.increase_height(self._get_delta(self.box.get_height()))

    def get_width(self) -> float:
        return self.box.get_width() + (2 * self._notch.h)

    def get_height(self) -> float:
        return self.box.get_height() + (2 * self._notch.h)

    def get_depth(self) -> float:
        return self.box.get_depth()

    def get_wall_x(self) -> float:
        return self.box.get_wall_x() + self._notch.h

    def get_wall_y(self) -> float:
        return self.box.get_wall_y() + self._notch.h

    def get_wall_z(self) -> float:
        return self.box.get_wall_z()

    def scad(self):
        print(f"created object with joints {self.get_width()}mm x {self.get_height()}mm x {self.get_depth()}mm")

        result = union()(self.box.scad(), self._joints)
        result = translate([self._notch.h, self._notch.h, 0])(result)
        return result

if __name__ == '__main__':
    obj = WithJoints(EmptyBox(Cube(10,20,30)))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
