from solid import *
from solid.utils import *

from parametrizedBox.helpers.Chamfer import *

from parametrizedBox.interior.Interior import *

class Cube(Interior):
    def __init__(self, width: float, height: float, depth: float):
        Interior.__init__(self, width, height, depth)

    def get_roof(self, depth) -> OpenSCADObject:
        return  chamfer(self)

    def scad(self):
        return cube([self.width, self.height, self.depth])

if __name__ == '__main__':
    obj = Cube(26, 105, 31)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")