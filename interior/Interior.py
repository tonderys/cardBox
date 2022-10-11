from solid import *
from solid.utils import *

class Interior:
    def __init__(self, width: float, height: float, depth: float):
        self.width = width
        self.height = height
        self.depth = depth

    def get_boundaries(self) -> OpenSCADObject:
        return cube([self.width, self.height, self.depth])

    def get_roof(self, depth) -> OpenSCADObject:
        roof = up(self.depth - depth)(cube([self.width, self.height, depth]))
        return intersection()(roof, self.scad())

    def scad(self) -> OpenSCADObject:
        return intersection()(self.body, self.get_boundaries())