from numpy import *
from solid import *
from solid.utils import *

from PrinterConstants import *
from Cube import Cube

class Bowl(Cube):
    def __init__(self, width: float, height: float, depth:float):
        Cube.__init__(self, width, height, depth)
        r = depth / 2
        inside = translate([r,r,r])(sphere(r = r, segments = 100))
        outside = cube([depth, depth, depth / 2])

        self.body = intersection()(inside, outside)
        self.body = scale([width/depth, height/depth, 2])(self.body)

    def scad(self) -> OpenSCADObject:
        return self.body

if __name__ == '__main__':
    obj = difference()(cube([50, 75, 20]), Bowl(50, 75, 20).scad())
    scad_render_to_file(obj, f"f:\\Druk3D\\STL\\openSCAD\\test2.scad")
