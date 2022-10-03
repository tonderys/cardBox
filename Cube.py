from solid import *
from solid.utils import *
class Cube:
    def __init__(self, width: float, height: float, depth: float):
        self.width = width
        self.height = height
        self.depth = depth

    def get_roof(self, depth) -> OpenSCADObject:
        roof = up(self.depth - depth)(cube([self.width, self.height, depth]))
        return difference()(roof, difference()(roof, self.scad()))

    def scad(self) -> OpenSCADObject:
        return cube([self.width, self.height,self.depth])