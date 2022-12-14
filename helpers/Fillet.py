from solid import *
from solid.utils import  *

from parametricBox.Box import Box

def get_all_combinations(delta_x, delta_y, delta_z, obj: Box, offset: float= 0):
    return [[[translate([offset + x, offset + y, offset + z])(obj) for x in delta_x] for y in delta_y] for z in delta_z]

def get_excess(obj: Box, r: float):
    height = obj.height - r
    width = obj.width - r
    depth = obj.depth - r

    cube_x = cube([obj.width,r,r])
    cube_y = cube([r,obj.height,r])
    cube_z = cube([r,r,obj.depth])

    return (get_all_combinations(delta_x = [0], delta_y = [0, height], delta_z = [0, depth], obj = cube_x) +
            get_all_combinations(delta_x = [0, width], delta_y = [0], delta_z = [0, depth], obj = cube_y) +
            get_all_combinations(delta_x = [0, width], delta_y = [0, height], delta_z = [0], obj = cube_z))

def get_trimmed_corners(obj: Box, r: float):
    segments = 20

    height = obj.height - (2 * r)
    width = obj.width - (2 * r)
    depth = obj.depth - (2 * r)

    corner = sphere(r=r, segments=segments)
    column_z = cylinder(r=r, h=depth, segments=segments)
    column_x = rot_z_to_x(cylinder(r=r, h=width, segments=segments))
    column_y = rot_z_to_y(cylinder(r=r, h=height, segments=segments))

    return (get_all_combinations([0, width], [0, height], [0, depth], corner, offset=r) +
            get_all_combinations([0, width], [0, height], [0], column_z, offset=r) +
            get_all_combinations([0], [0, height], [0, depth], column_x, offset=r) +
            get_all_combinations([0, width], [0], [0, depth], column_y, offset=r))


class Fillet:
    def __init__(self, obj: Box, r: float = 2):
        self.excess = difference()(
            union()([e for e in get_excess(obj, r)]),
            union()([c for c in get_trimmed_corners(obj, r)]))

    def scad(self) -> OpenSCADObject:
        return self.excess

if __name__ == '__main__':
    from parametricBox.PlainBox import *

    obj = Fillet(PlainBox(Cube(15, 15, 30)), 2)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
