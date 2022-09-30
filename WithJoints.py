from numpy import arange
import solid
from solid.utils import *


class Notch:
    def __init__(self, height):
        self.printer_gap = 0.2
        self.a = 6
        self.b = 3
        self.delta = (self.a - self.b) / 2
        self.h = self.delta
        self.height = height

    def _down_left(self, height):
        return [0 + (self.printer_gap / 2), 0, height]

    def _down_right(self, height):
        return [self.b - (self.printer_gap / 2), 0, height]

    def _up_right(self, height):
        return [self.b + self.delta - (self.printer_gap / 2), self.h, height]

    def _up_left(self, height):
        return [-self.delta + (self.printer_gap / 2), self.h, height]

    def _first_up_left(self, height):
        return [0, self.h, height]

    def get_interlocked_length(self):
        return self.a + self.b

    def get_delta(self):
        return self.delta

    def first_scad(self):
        return solid.polyhedron(points=[self._down_left(0),
                                        self._down_right(0),
                                        self._up_right(0),
                                        self._first_up_left(0),
                                        self._down_left(self.height),
                                        self._down_right(self.height),
                                        self._up_right(self.height),
                                        self._first_up_left(self.height)],
                                faces=[[0, 1, 2, 3],
                                       [4, 5, 1, 0],
                                       [5, 6, 2, 1],
                                       [6, 7, 3, 2],
                                       [7, 4, 0, 3],
                                       [7, 6, 5, 4]])

    def scad(self):
        return solid.polyhedron(points=[self._down_left(0),
                                        self._down_right(0),
                                        self._up_right(0),
                                        self._up_left(0),
                                        self._down_left(self.height),
                                        self._down_right(self.height),
                                        self._up_right(self.height),
                                        self._up_left(self.height)],
                                faces=[[0, 1, 2, 3],
                                       [4, 5, 1, 0],
                                       [5, 6, 2, 1],
                                       [6, 7, 3, 2],
                                       [7, 4, 0, 3],
                                       [7, 6, 5, 4]])


class WithJoints:
    def __init__(self, box):
        self.box = box
        self.notch = Notch(self.box.outer.depth)
        self._adjust_walls()
        self.joints = [self._get_upper_joints(), self._get_right_joints(), self._get_lower_joints(),
                       self._get_left_joints()]

    def _get_upper_joints(self):
        joint = self.notch.scad()
        return solid.translate([0, self.box.outer.height, 0])(self.notch.first_scad()) + \
               [solid.translate([i, self.box.outer.height, 0])(joint)
                   for i in arange(self.notch.get_interlocked_length(),
                                   self.box.outer.width,
                                   self.notch.get_interlocked_length())]

    def _get_right_joints(self):
        joint = rotate([0, 0, -90])(self.notch.scad())
        return solid.translate([self.box.outer.width, self.box.outer.height, 0])(rotate([0, 0, -90])(self.notch.first_scad())) + \
               [solid.translate([self.box.outer.width, self.box.outer.height - i, 0])(joint)
                for i in arange(self.notch.get_interlocked_length(),
                               self.box.outer.height,
                               self.notch.get_interlocked_length())]

    def _get_lower_joints(self):
        joint = rotate([0, 0, -180])(self.notch.scad())
        return solid.translate([self.box.outer.width, 0, 0])(rotate([0, 0, -180])(self.notch.first_scad())) + \
               [solid.translate([self.box.outer.width - i, 0, 0])(joint)
                for i in arange(self.notch.get_interlocked_length(),
                               self.box.outer.width,
                               self.notch.get_interlocked_length())]

    def _get_left_joints(self):
        joint = rotate([0, 0, -270])(self.notch.scad())
        return solid.translate([0, 0, 0])(rotate([0, 0, -270])(self.notch.first_scad())) + \
               [solid.translate([0, i, 0])(joint)
                for i in arange(self.notch.get_interlocked_length(),
                               self.box.outer.height,
                               self.notch.get_interlocked_length())]

    def _get_delta(self, length):
        mod = length % self.notch.get_interlocked_length()
        if mod == 0: return 0
        delta = self.notch.get_interlocked_length() - mod - self.notch.get_delta()
        return delta if delta > 0 else delta + self.notch.get_interlocked_length()

    def _adjust_walls(self):
        self.box.increase_width(self._get_delta(self.box.outer.width))
        self.box.increase_height(self._get_delta(self.box.outer.height))

    def scad(self):
        return solid.union()(self.box.scad(), self.joints)
