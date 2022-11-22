from numpy import *
from solid.utils import *

from parametricBox.Box import *
from parametricBox.helpers.Notch import *

class WithJoints(Box):
    def __init__(self, box: Box):
        self.box = box
        self._notch = Notch(self.box.depth)

        Box.__init__(self, self.box.width,
                           self.box.height,
                           self.box.depth)
        joints = [self._get_upper_joints(), self._get_right_joints(),
                  self._get_lower_joints(), self._get_left_joints()]
        body = union()(self._move_by_delta()(self.box.scad()), self._get_case(), joints)

        self.width += 2 * self._notch.h
        self.height += 2 * self._notch.h
        self.body = translate([self._notch.h, self._notch.h, 0])(body)

    def _get_joints(self, length):
        joint = self._notch.scad()
        joints = union()([translate([i, 0, 0])(joint) for i in arange(0,length, self._notch.get_interlocked_length())])
        return intersection()(cube([length, self._notch.h, self._notch.height]), joints)

    def _get_upper_joints(self):
        delta = self._get_delta(self.width)
        self.width += delta
        joints = self._get_joints(self.width)
        return forward(self.height)(joints)

    def _get_right_joints(self):
        delta = self._get_delta(self.height)
        self.height += delta
        joints = self._get_joints(self.height)
        joints = rotate([0, 0, -90])(joints)
        return translate([self.width, self.height, 0])(joints)

    def _get_lower_joints(self):
        delta = self._get_delta(self.width)
        self.width += delta
        joints = self._get_joints(self.width)
        joints = rotate([0, 0, 180])(joints)
        return right(self.width)(joints)

    def _get_left_joints(self):
        delta = self._get_delta(self.height)
        self.height += delta
        joints = self._get_joints(self.height)
        return rotate([0, 0, 90])(joints)

    def _get_delta(self, length):
        mod = length % self._notch.get_interlocked_length()
        if mod == self._notch.get_interlocked_length() - self._notch.delta: return 0
        delta = self._notch.get_interlocked_length() - mod - self._notch.delta
        return delta if delta > 0 else delta + self._notch.get_interlocked_length()

    def get_wall_x(self) -> float:
        return (self.width - self.box.box.width) / 2

    def get_wall_y(self) -> float:
        return (self.height - self.box.box.height) / 2


    def _get_case(self) -> OpenSCADObject:
        return difference()(
                cube([self.width,
                      self.height,
                      self.depth]),
                self._move_by_delta()(
                    cube([self.box.width,
                          self.box.height,
                          self.box.depth])))

    def _move_by_delta(self):
        return translate([(self.width - self.box.width) / 2,
                          (self.height - self.box.height) / 2,
                          0])

    def scad(self):
        return self.body

if __name__ == '__main__':
    from parametricBox.PlainBox import *

    obj = PlainBox(Cube(10, 20, 30))
    for i in range(3):
        obj = WithJoints(obj)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
