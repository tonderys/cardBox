from solid import *
from solid.utils import *

from parametricBox.helpers.Measured import *

class Interior(Measured):
    def __init__(self, name: str, width: float, height: float, depth: float):
        self.name = name
        Measured.__init__(self, width, height, depth)

    def get_boundaries(self) -> OpenSCADObject:
        return cube([self.width, self.height, self.depth])

    def log(self) -> str:
        return f"created {self.name} with width: {self.width}, height: {self.height} and depth: {self.depth}"

    def scad(self) -> OpenSCADObject:
        return intersection()(self.body, self.get_boundaries())