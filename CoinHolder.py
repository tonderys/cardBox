from numpy import *
from solid import *

from PrinterConstants import *
from Cube import Cube

class CoinHolder(Cube):
    def __init__(self, coin_diameter, depth, amount_of_columns):
        self.coin_hole = cylinder(d=coin_diameter, h=depth)
        self.finger_hole = cylinder(d=finger_diameter, h=depth)
        self.amount_of_columns = amount_of_columns

        finger_radius = finger_diameter / 2
        coin_radius = coin_diameter / 2
        pos = [finger_radius, finger_radius,0]
        self.holes = translate(pos)(self.finger_hole)

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.coin_hole))

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.finger_hole))

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] - ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.coin_hole))

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] - ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.finger_hole))

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.coin_hole))

        pos = [pos[0] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[1] + ((finger_radius + coin_radius) / sqrt(2)),
               pos[2] + 0]
        self.holes = union()(self.holes,
                             translate(pos)(self.finger_hole))

        Cube.__init__(self, pos[0] + finger_radius, pos[1] + finger_radius, depth)

    def scad(self):
        return self.holes