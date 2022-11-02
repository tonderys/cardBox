from solid import *
from solid.utils import *

from parametricBox.helpers.roof import *

from parametricBox.interior.Interior import *

class Pipe(Interior):
    def __init__(self, diameter, height, depth):
        Interior.__init__(self, "Pipe", diameter, height, depth)

        r = diameter / 2

        tokens = translate([r, 0, r])(rot_z_to_y(cylinder(d=diameter, h=height)))
        path = up(r)(cube([diameter, height, depth - r]))
        self.body = union()(tokens, path)

if __name__ == '__main__':
    obj = Pipe(25,105,31)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
