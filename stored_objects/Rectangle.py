from solid import *

from parametricBox.helpers.Measured import *

class Rectangle(Measured):
    def __init__(self, width: float, height: float, depth: float):
        Measured.__init__(self, width, height, depth)

    def __str__(self):
        return f"Rectangle({self.get_width()}x{self.get_height()}x{self.get_depth()})"

    def scad(self):
        return cube([self.get_width(), self.get_height(), self.get_depth()])

if __name__ == '__main__':
    obj = Rectangle(23, 8, 2)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
