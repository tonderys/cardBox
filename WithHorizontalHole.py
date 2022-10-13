from solid import *
from solid.utils import *

from Box import *
from WithJoints import *

class WithHorizontalHole(Box):
    def __init__(self, box: Box):
        Box.__init__(self, box.inner)
        self.box = box

    def get_width(self) -> float:
        return self.box.get_width()

    def get_height(self) -> float:
        return self.box.get_height()

    def get_depth(self) -> float:
        return self.box.get_depth()

    def get_wall_x(self) -> float:
        return self.box.get_wall_x()

    def get_wall_y(self) -> float:
        return self.box.get_wall_y()

    def get_floor(self) -> float:
        return self.box.get_floor()

    def scad(self) -> OpenSCADObject:
        diameter = min(0.8 * self.box.get_width(), finger_diameter)

        hole = rot_z_to_y(cylinder(d=diameter, h=self.box.get_height()))
        hole = union()(hole,
                       left(diameter / 2)(
                           cube([diameter,
                                 self.box.get_height(),
                                 self.box.get_depth() / 2])))
        hole = translate([self.box.get_width() / 2,
                          0,
                          self.box.get_depth() / 2])(hole)

        self.bottom = difference()(self.box.scad(), hole)
        return self.bottom

if __name__ == '__main__':
    obj = WithHorizontalHole(WithJoints(Box(Cube(100, 20, 30))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
