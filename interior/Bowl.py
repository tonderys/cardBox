from numpy import *
from solid import *
from solid.utils import *

from parametricBox.interior.Interior import *

class Bowl(Interior):
    def __init__(self, width: float, height: float, depth:float):
        Interior.__init__(self, "Bowl", width, height, depth)
        r = depth / 2
        inside = translate([r,r,r])(sphere(r = r, segments = 100))

        self.body = scale([width/depth, height/depth, 2])(inside)

if __name__ == '__main__':
    obj = Bowl(50, 75, 20).scad()
    scad_render_to_file(obj, f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
