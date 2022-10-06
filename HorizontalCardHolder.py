from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *
from MeasuredObject import *

def get_holes(obj: MeasuredObject, diameter: float) -> OpenSCADObject:
    hole = union()(cylinder(d=diameter, h=obj.get_wall_z(), segments=36),
                   back(diameter / 2)(cube([obj.get_wall_x(), diameter, obj.get_depth()])))
    holes = [right(obj.get_width() - obj.get_wall_x())(hole),
             right(obj.get_wall_x())(rotate([0, 0, 180])(hole))]
    return [forward(obj.get_height() / 2)(hole) for hole in holes]

class HorizontalCardHolder():
    def __init__(self, interior: Cube):
        base = EmptyBox(interior)
        base.thicken_floor(2.0)
        self.body = WithJoints(base)
        self.body.box.chamfer_inside()

    def scad(self) -> OpenSCADObject:
        diameter = min(0.8 * self.body.get_width(), finger_diameter)
        return difference()(self.body.scad(), get_holes(self.body, diameter))

if __name__ == '__main__':
    obj = HorizontalCardHolder(Cube(26,105,31))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")