from solid import *
from solid.utils import *

from parametricBox.interior.Interior import *

class Column(Interior):
    def __init__(self, diameter, depth, segments:float = 16):
        Interior.__init__(self, "Column", diameter, diameter, depth)

        r = diameter / 2

        self.body = translate([r, r, 0])(cylinder(d=diameter, h=depth, segments = segments))

if __name__ == '__main__':
    obj = Column(7.5,13,6)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
