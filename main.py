from solid import *
from solid.utils import *

def move_to_center_top(delta):
    return translate((delta,
                      delta,
                      delta))

class Empty_box(OpenSCADObject):
    def __init__(self, width, height, depth, wall_thickness):
        self.wall_thickness = wall_thickness
        self.outer = cube([width + (2 * wall_thickness),
                           height + (2 * wall_thickness),
                           depth + (2 * wall_thickness)])
        self.inner = move_to_center_top(wall_thickness)(cube([width, height, depth + wall_thickness]))

    def get(self):
        return difference()(self.outer, self.inner)

class Card_holder(OpenSCADObject):
    def __init__(self, width, height, depth, wall_thickness):
        radius = 10

        hole = forward(height / 2)(cylinder(h=depth + 2 * wall_thickness, r=radius))
        self.box = Empty_box(width, height, depth, wall_thickness).get()
        self.holes = [hole, right(width + (2*wall_thickness))(hole)]

        roof = (move_to_center_top(wall_thickness)(up(depth)(cube([width,height, wall_thickness]))))
        flaps = union()([intersection()(self.box, hole) for hole in self.holes])
        flaps = difference()(flaps, down(depth + wall_thickness)(roof))

        joint = Joint(depth + (2 * wall_thickness)).get()
        joints = []
        for i in range(1, width + (2 * wall_thickness), 6):
            joints.append(translate([i, height + (2 * wall_thickness), 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, height + (2 * wall_thickness), 6):
            joints.append(translate([width + (2 * wall_thickness), height + (2 * wall_thickness) - i, 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, width + (2 * wall_thickness), 6):
            joints.append(translate([width + (2 * wall_thickness) - i, 0, 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, height + (2 * wall_thickness), 6):
            joints.append(translate([0, i, 0])(joint))

        self.top = union()(roof, flaps)
        self.bottom = union()(self.box, joints)
        self.bottom = difference()(self.bottom, self.holes)

    def get_top(self):
        return self.top

    def get_bottom(self):
        return self.bottom

class Joint:
    def __init__(self, h):
        self.body = polyhedron(points=[[0,0,0],[2,0,0],[3,1,0],[-1,1,0],[0,0,h],[2,0,h],[3,1,h],[-1,1,h]],
                               faces =[[0,1,2,3],[4,5,1,0],[5,6,2,1],[6,7,3,2], [7,4,0,3],[7,6,5,4]])
    def get(self):
        return self.body

def main():
    width = 63
    height = 88
    depth = 20
    wall_thickness = 5

    object = Card_holder(width, height, depth, wall_thickness)

    scad_render_to_file(object.get_top(), f"top_{width}x{height}mm.scad")
    scad_render_to_file(object.get_bottom(), f"bottom_{width}x{height}mm.scad")

main()