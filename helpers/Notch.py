from solid import *
from parametrizedBox.helpers.PrinterConstants import *
class Notch:
    def __init__(self, height: float):
        self.a = 6
        self.b = 3
        self.delta = (self.a - self.b) / 2
        self.h = self.delta
        self.height = height

    def _down_left(self, height: float) -> P3:
        return [0 + (printer_gap / 2), 0, height]

    def _down_right(self, height: float) -> P3:
        return [self.b - (printer_gap / 2), 0, height]

    def _up_right(self, height: float) -> P3:
        return [self.b + self.delta - (printer_gap / 2), self.h, height]

    def _up_left(self, height: float) -> P3:
        return [-self.delta + (printer_gap / 2), self.h, height]

    def get_interlocked_length(self) -> float:
        return self.a + self.b

    def scad(self) -> OpenSCADObject:
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

if __name__ == '__main__':
    obj = Notch(10)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
