from solid import *
from solid.utils import *

from parametrizedBox.interior.Pipe import *
from parametrizedBox.PlainBox import *
from parametrizedBox.WithJoints import *
from parametrizedBox.WithHorizontalHole import *

def get_holes(obj: Box, diameter: float) -> OpenSCADObject:
    hole = union()(cylinder(d=diameter, h=obj.get_floor(), segments=36),
                   back(diameter / 2)(cube([obj.get_wall_x(), diameter, obj.get_depth()])))
    holes = [right(obj.get_width() - obj.get_wall_x())(hole),
             right(obj.get_wall_x())(rotate([0, 0, 180])(hole))]
    return [forward(obj.get_height() / 2)(hole) for hole in holes]

class WithVerticalHoles(Box):
    def __init__(self, box: Box):
        self.box = box
        self.box.thicken_floor(2.0)

    def scad(self) -> OpenSCADObject:
        diameter = min(0.8 * self.get_width(), finger_diameter)
        return difference()(self.box.scad(), get_holes(self, diameter))

if __name__ == '__main__':
    obj = WithHorizontalHole(WithVerticalHoles(WithJoints(PlainBox(Cube(26, 105, 31)))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")