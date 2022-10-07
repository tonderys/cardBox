from solid import *
from solid.utils import  *
from MeasuredObject import *
from EmptyBox import *

def get_all_combinations(delta_x, delta_y, delta_z, obj):
    return [[[translate([x,y ,z])(obj) for x in delta_x] for y in delta_y] for z in delta_z]

class Fillet:
    def __init__(self, obj: MeasuredObject, r: float):
        corner = sphere(r = r, segments = 20)

        height = obj.get_height() - (2 * r)
        width = obj.get_width() - (2 * r)
        depth = obj.get_depth() - (2 * r)

        corners = get_all_combinations([0,width], [0, height], [0,depth], corner)
        # corners = [translate([0    , 0     , 0    ])(corner),
        #            translate([0    , 0     , depth])(corner),
        #            translate([width, 0     , 0    ])(corner),
        #            translate([0    , height, 0    ])(corner),
        #            translate([width, height, 0    ])(corner),
        #            translate([width, 0     , depth])(corner),
        #            translate([0    , height, depth])(corner),
        #            translate([width, height, depth])(corner)]
        self.corners = [translate([r,r,r])(c) for c in corners]

        column_z = cylinder(r=r, h=depth, segments = 20)
        up_columns = [column_z,
                      translate([width, height, 0])(column_z),
                      translate([width, 0     , 0])(column_z),
                      translate([0    , height, 0])(column_z)]
        self.z_columns = [translate([r,r,r])(uc) for uc in up_columns]

        column_x = rot_z_to_x(cylinder(r=r, h=width, segments = 20))
        x_columns = [column_x,
                      translate([0, 0     , depth])(column_x),
                      translate([0, height, 0    ])(column_x),
                      translate([0, height, depth])(column_x)]
        self.x_columns = [translate([r,r,r])(uc) for uc in x_columns]

        column_y = rot_z_to_y(cylinder(r=r, h=height, segments = 20))
        y_columns = [column_y,
                      translate([width, 0, 0    ])(column_y),
                      translate([0    , 0, depth])(column_y),
                      translate([width, 0, depth])(column_y)]
        self.y_columns = [translate([r,r,r])(uc) for uc in y_columns]

        height = obj.get_height() - r
        width = obj.get_width() - r
        depth = obj.get_depth() - r

        cube_x = cube([obj.get_width(),r,r])
        self.x_cubes = [cube_x,
                        translate([0, 0     , depth])(cube_x),
                        translate([0, height, 0    ])(cube_x),
                        translate([0, height, depth])(cube_x)]

        cube_y = cube([r,obj.get_height(),r])
        self.y_cubes = [cube_y,
                        translate([width, 0, 0    ])(cube_y),
                        translate([width, 0, depth])(cube_y),
                        translate([0    , 0, depth])(cube_y)]

        cube_z = cube([r,r,obj.get_depth()])
        self.z_cubes = [cube_z,
                        translate([width, 0     , 0])(cube_z),
                        translate([0    , height, 0])(cube_z),
                        translate([width, height, 0])(cube_z)]


    def scad(self) -> OpenSCADObject:
        return difference()(union()([c for c in self.x_cubes], [c for c in self.y_cubes], [c for c in self.z_cubes]),
                            union()([c for c in self.corners], [c for c in self.z_columns], [c for c in self.x_columns], [c for c in self.y_columns]))

if __name__ == '__main__':
    obj = Fillet(EmptyBox(Cube(10,20,30)), 2)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
