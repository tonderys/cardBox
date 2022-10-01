from solid import *

class Cube:
    def __init__(self, width: float, height: float, depth: float):
        self.width = width
        self.height = height
        self.depth = depth

    def scad(self) -> OpenSCADObject:
        return cube([self.width, self.height,self.depth])