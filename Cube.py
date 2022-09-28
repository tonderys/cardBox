from solid import *

class Cube:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def scad(self):
        return cube([self.width, self.height,self.depth])