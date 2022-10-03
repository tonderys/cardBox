from solid import *
from solid.utils import *

from Cube import *
from PrinterConstants import *
from MeasuredObject import *
from Chamfer import *

class EmptyBox(MeasuredObject):
    def __init__(self, inner: Cube):
        self.chamfered = False
        self._outer = Cube(inner.width + (2 * min_wall_thickness),
                           inner.height + (2 * min_wall_thickness),
                           inner.depth + (2 * min_wall_thickness))
        self.inner = inner
        self.roof = translate([self.get_wall_x(), self.get_wall_y(), 2 * self.get_wall_z()])(inner.get_roof(self.get_wall_z()))

    def get_width(self):
        return self._outer.width

    def get_height(self):
        return self._outer.height

    def get_depth(self):
        return self._outer.depth

    def increase_width(self, delta: float):
        self._outer.width += delta
        self.roof = right(delta/2)(self.roof)

    def increase_height(self, delta: float):
        self._outer.height += delta
        self.roof = forward(delta/2)(self.roof)

    def increase_depth(self, delta: float):
        self._outer.deptht += delta
        self.roof = up(delta/2)(self.roof)

    def get_wall_x(self) -> float:
        return (self.get_width() - self.inner.width) / 2

    def get_wall_y(self) -> float:
        return (self.get_height() - self.inner.height) / 2

    def get_wall_z(self) -> float:
        return (self.get_depth() - self.inner.depth) / 2

    def chamfer_inside(self) -> OpenSCADObject:
        self.roof = chamfer(self)

    def scad(self) -> OpenSCADObject:
        outer = difference()(self._outer.scad(), self.roof)

        inner = translate((self.get_wall_x(),
                           self.get_wall_y(),
                           self.get_wall_z()))(self.inner.scad())

        return difference()(outer, inner)

if __name__ == '__main__':
    obj = EmptyBox(Cube(26,105,31))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")