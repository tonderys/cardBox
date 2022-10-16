from numpy import *

from parametrizedBox.helpers.Fillet import *
from parametrizedBox.helpers.Notch import *
from parametrizedBox.PlainBox import *

class WithJoints(Box):
    def __init__(self, box: Box):
        self.box = box
        self._notch = Notch(self.box.get_depth())

        self.width = self.box.get_width() + self._get_delta(self.box.get_width())
        self.height = self.box.get_height() + self._get_delta(self.box.get_height())

    def _get_joints(self, length):
        assert((length + self._notch.delta) % self._notch.get_interlocked_length() == 0)
        joint = self._notch.scad()
        joints = union()([translate([i, 0, 0])(joint) for i in arange(0,length, self._notch.get_interlocked_length())])
        return intersection()(cube([length, self._notch.h, self._notch.height]), joints)

    def _get_upper_joints(self):
        joints = self._get_joints(self.width)
        return forward(self.height)(joints)

    def _get_right_joints(self):
        joints = self._get_joints(self.height)
        joints = rotate([0, 0, -90])(joints)
        return translate([self.width, self.height, 0])(joints)

    def _get_lower_joints(self):
        joints = self._get_joints(self.width)
        joints = rotate([0, 0, 180])(joints)
        return right(self.width)(joints)

    def _get_left_joints(self):
        joints = self._get_joints(self.height)
        return rotate([0, 0, 90])(joints)

    def _get_delta(self, length):
        mod = length % self._notch.get_interlocked_length()
        if mod == self._notch.get_interlocked_length() - self._notch.delta: return 0
        delta = self._notch.get_interlocked_length() - mod - self._notch.delta
        return delta if delta > 0 else delta + self._notch.get_interlocked_length()

    def get_width(self) -> float:
        return self.width + (2 * self._notch.h)

    def get_height(self) -> float:
        return self.height + (2 * self._notch.h)

    def get_depth(self) -> float:
        return self.box.get_depth()

    def get_wall_x(self) -> float:
        return (self.get_width() - self.box.box.get_width()) / 2

    def get_wall_y(self) -> float:
        return (self.get_height() - self.box.box.get_height()) / 2

    def get_floor(self) -> float:
        return self.box.get_floor()

    def thicken_floor(self, delta: float):
        self.box.thicken_floor(delta)

    def _get_case(self) -> OpenSCADObject:
        return difference()(
                cube([self.width,
                      self.height,
                      self.get_depth()]),
                self._move_by_delta()(
                    cube([self.box.get_width(),
                          self.box.get_height(),
                          self.box.get_depth()])))

    def _move_by_delta(self):
        return translate([(self.width - self.box.get_width()) / 2,
                          (self.height - self.box.get_height()) / 2,
                          0])

    def scad(self):
        joints = [self._get_upper_joints(), self._get_right_joints(),
                  self._get_lower_joints(), self._get_left_joints()]
        body = union()(self._move_by_delta()(self.box.scad()), self._get_case(), joints)

        return translate([self._notch.h, self._notch.h, 0])(body)

if __name__ == '__main__':
    obj = PlainBox(Cube(10, 20, 30))
    for i in range(3):
        obj = WithJoints(obj)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
