from solid import *
from solid.utils import *

from parametricBox.interior.Pipe import *
from parametricBox.PlainBox import *
from parametricBox.WithJoints import *
from parametricBox.WithHorizontalHole import *

def get_holes(obj: Box, diameter: float) -> OpenSCADObject:
    diameter = min(0.4 * obj.get_width(), diameter)

    hole = union()(cylinder(d=diameter, h=obj.get_floor(), segments=36),
                   back(diameter / 2)(cube([obj.get_wall_x(), diameter, obj.get_depth()])))
    holes = [right(obj.get_width() - obj.get_wall_x())(hole),
             right(obj.get_wall_x())(rotate([0, 0, 180])(hole))]
    return [forward(obj.get_height() / 2)(hole) for hole in holes]

    def log(self) -> str:
        return f"{self.box.log()}  {type(self).__name__}"

class WithVerticalHoles(Box):
    def __init__(self, box: Box, floor_delta: float = 2.0):
        self.floor_delta = floor_delta

        self.box = box
        floor = intersection()(self.box.scad(),
                                    cube([self.box.get_width(),
                                          self.box.get_height(),
                                          self.box.get_floor()]))
        floor = scale([1, 1, self.floor_delta / self.box.get_floor()])(floor)
        self.body = union()(up(self.floor_delta)(self.box.scad()), floor)

    def get_floor(self) -> float:
        return self.box.get_floor() + self.floor_delta

    def get_depth(self) -> float:
        return self.box.get_depth() + self.floor_delta

    def scad(self) -> OpenSCADObject:
        diameter = min(0.8 * self.get_width(), finger_diameter)
        return difference()(self.body, get_holes(self, diameter))

if __name__ == '__main__':
    obj = WithVerticalHoles(WithJoints(PlainBox(Cube(26, 105, 31))))
    print(obj.log())
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")