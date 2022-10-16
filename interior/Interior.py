from solid import *
from solid.utils import *

class Interior:
    def __init__(self, name: str, width: float, height: float, depth: float):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_depth(self):
        return self.depth

    def get_boundaries(self) -> OpenSCADObject:
        return cube([self.width, self.height, self.depth])

    def get_roof(self, depth) -> OpenSCADObject:
        roof = up(self.depth - depth)(cube([self.width, self.height, depth]))
        return intersection()(roof, self.scad())

    def log(self) -> str:
        return f"created {self.name} with width: {self.width}, height: {self.height} and depth: {self.depth}"

    def scad(self) -> OpenSCADObject:
        return intersection()(self.body, self.get_boundaries())