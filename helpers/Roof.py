from solid import *
from solid.utils import *

from parametricBox.helpers.Measured import *

def chamfer(box: Measured, chamfer_depth: float = 2.0) -> OpenSCADObject:
    return polyhedron(points=[[0, 0, box.depth - chamfer_depth],
                              [0, box.height, box.depth - chamfer_depth],
                              [box.width, box.height, box.depth - chamfer_depth],
                              [box.width, 0, box.depth - chamfer_depth],
                              [-chamfer_depth, -chamfer_depth, box.depth],
                              [-chamfer_depth, box.height + chamfer_depth, box.depth],
                              [box.width + chamfer_depth, box.height + chamfer_depth, box.depth],
                              [box.width + chamfer_depth, -chamfer_depth, box.depth]],
                      faces=[[0, 1, 2, 3],
                             [4, 5, 1, 0],
                             [5, 6, 2, 1],
                             [6, 7, 3, 2],
                             [7, 4, 0, 3],
                             [7, 6, 5, 4]])

def regular(box: Measured, chamfer_depth: float = 2.0) -> OpenSCADObject:
    roof = up(box.depth - chamfer_depth)(cube([box.width, box.height, chamfer_depth]))
    return intersection()(roof, box.scad())
