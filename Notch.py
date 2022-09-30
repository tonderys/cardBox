from solid import *

class Notch:
    def __init__(self, height):
        self.printer_gap = 0.2
        self.a = 6
        self.b = 3
        self.delta = (self.a - self.b) / 2
        self.h = self.delta
        self.height = height

    def _down_left(self, height):
        return [0 + (self.printer_gap / 2), 0, height]

    def _down_right(self, height):
        return [self.b - (self.printer_gap / 2), 0, height]

    def _up_right(self, height):
        return [self.b + self.delta - (self.printer_gap / 2), self.h, height]

    def _up_left(self, height):
        return [-self.delta + (self.printer_gap / 2), self.h, height]

    def get_interlocked_length(self):
        return self.a + self.b

    def scad(self):
        return polyhedron(points=[self._down_left(0),
                                        self._down_right(0),
                                        self._up_right(0),
                                        self._up_left(0),
                                        self._down_left(self.height),
                                        self._down_right(self.height),
                                        self._up_right(self.height),
                                        self._up_left(self.height)],
                                faces=[[0, 1, 2, 3],
                                       [4, 5, 1, 0],
                                       [5, 6, 2, 1],
                                       [6, 7, 3, 2],
                                       [7, 4, 0, 3],
                                       [7, 6, 5, 4]])
