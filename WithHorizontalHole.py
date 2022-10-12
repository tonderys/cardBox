from solid import *
from solid.utils import *

from Box import *
from WithJoints import *

class WithHorizontalHole(Box):
    def __init__(self, box: Box):
        Box.__init__(self, box.inner)
        self.box = box

        diameter = min(0.8 * box.get_width(), finger_diameter)

        hole = rot_z_to_y(cylinder(d=diameter, h=box.get_height()))
        hole = union()(hole, left(diameter / 2)(cube([diameter, box.get_height(), box.get_depth() / 2])))
        hole = translate([box.get_width() / 2,
                          0,
                          box.get_depth() / 2])(hole)

        self.bottom = difference()(box.scad(), hole)

    def scad(self) -> OpenSCADObject:
        return self.bottom

if __name__ == '__main__':
    obj = WithHorizontalHole(WithJoints(Box(Cube(100, 20, 30))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
