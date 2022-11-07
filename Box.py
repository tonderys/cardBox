from parametricBox.helpers.Measured import *

class Box(Measured):
    def __init__(self, width, height, depth):
        Measured.__init__(self, width, height, depth)

    def get_wall_x(self) -> float:
        return self.box.get_wall_x()

    def get_wall_y(self) -> float:
        return self.box.get_wall_y()

    def get_floor(self) -> float:
        return self.box.get_floor()

    def log(self) -> str:
        return self.box.log() + "\n" + \
               f"created {type(self).__name__} " + \
               f"with dimensions {self.width}(w) x {self.height}(h) x {self.depth}(d) " + \
               f"and walls {self.get_wall_x()}(x) {self.get_wall_y()}(y) {self.get_floor()}(floor)"

    def scad(self):
        pass