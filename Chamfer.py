from solid import *

from EmptyBox import *

def chamfer(box) -> OpenSCADObject:
    return polyhedron(points=[[box.get_wall_x(), box.get_wall_y(), box.get_depth() * 0.8],
                              [box.get_wall_x(), box.get_height() - box.get_wall_y(), box.get_depth() * 0.8],
                              [box.get_width() - box.get_wall_x(), box.get_height() - box.get_wall_y(), box.get_depth() * 0.8],
                              [box.get_width() - box.get_wall_x(), box.get_wall_y(), box.get_depth() * 0.8],
                              [box.get_wall_x() / 2, box.get_wall_y() / 2, box.get_depth()],
                              [box.get_wall_x() / 2, box.get_height() - (box.get_wall_y() / 2), box.get_depth()],
                              [box.get_width() - (box.get_wall_x() / 2), box.get_height() - (box.get_wall_y() / 2), box.get_depth()],
                              [box.get_width() - (box.get_wall_x() / 2), box.get_wall_y() / 2, box.get_depth()]],
                      faces=[[0, 1, 2, 3],
                             [4, 5, 1, 0],
                             [5, 6, 2, 1],
                             [6, 7, 3, 2],
                             [7, 4, 0, 3],
                             [7, 6, 5, 4]])
