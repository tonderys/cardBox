from solid import *
from solid.utils import *

from parametricBox.helpers.Chamfer import *

from parametricBox.interior.Interior import *

class Cube(Interior):
    def __init__(self, width: float, height: float, depth: float):
        Interior.__init__(self, "Cube", width, height, depth)
        self.body = cube([self.width, self.height, self.depth])

    def get_roof(self, depth) -> OpenSCADObject:
        return chamfer(self)

if __name__ == '__main__':
    obj = Cube(26, 105, 31)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")