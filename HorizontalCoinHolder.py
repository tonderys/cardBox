from numpy import *
from solid import *
from solid.utils import *

from PrinterConstants import *
from Cube import Cube

class HorizontalCoinHolder(Cube):
    def __init__(self, coin_diameter, height, depth):
        Cube.__init__(self, coin_diameter, height + coin_diameter, depth)

        coin_radius = coin_diameter / 2

        coins = translate([coin_radius, coin_radius, coin_radius])(rot_z_to_y(cylinder(d=coin_diameter, h=height)))
        path = translate([0,coin_radius, coin_radius])(cube([coin_diameter, height, depth - coin_radius]))
        finger = translate([coin_radius, coin_radius, coin_radius])(
                        union()(sphere(d=coin_diameter),
                                cylinder(d=coin_diameter, h=depth - coin_radius)))
        fingers = union()(finger,
                          forward(height)(finger))
        self.body = union()(coins, path, fingers)

    def scad(self) -> OpenSCADObject:
        return self.body

if __name__ == '__main__':
    obj = HorizontalCoinHolder(26,105,31)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
