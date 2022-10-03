from numpy import *
from solid import *
from solid.utils import *

from PrinterConstants import *
from Cube import Cube

class HorizontalCoinHolder(Cube):
    def __init__(self, coin_diameter, height, depth):
        coin_radius = coin_diameter / 2
        self.coin_hole = cylinder(d=coin_diameter, h=depth)

        self.hole = translate([coin_radius, coin_radius, coin_radius])(rot_z_to_y(cylinder(d=coin_diameter, h=height)))
        self.hole = union()(self.hole, translate([0,coin_radius, coin_radius])(cube([coin_diameter, height, depth - coin_radius])))
        finger_hole = union()(sphere(d=coin_diameter), cylinder(d=coin_diameter, h=depth - coin_radius))
        finger_hole = translate([coin_radius, coin_radius, coin_radius])(finger_hole)

        self.hole = union()(self.hole, finger_hole, forward(height)(finger_hole))

        Cube.__init__(self, coin_diameter, height + coin_diameter, depth)

    def scad(self) -> OpenSCADObject:
        return self.hole

if __name__ == '__main__':
    obj = HorizontalCoinHolder(26,105,31)
    scad_render_to_file(obj.get_roof(1), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
