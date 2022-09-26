from solid import *
from solid.utils import *

def move_to_center_top(delta):
    return translate((delta,
                      delta,
                      delta))

class empty_box(OpenSCADObject):
    def __init__(self, width, height, depth, wall_thickness):
        self.wall_thickness = wall_thickness
        self.outer = cube([width + (2 * wall_thickness),
                           height + (2 * wall_thickness),
                           depth + (2 * wall_thickness)])
        self.inner = move_to_center_top(wall_thickness)(cube([width, height, depth + wall_thickness]))

    def get(self):
        return difference()(self.outer, self.inner)

class card_holder(OpenSCADObject):
    def __init__(self, width, height, depth, wall_thickness):
        radius = 10

        hole = forward(height / 2)(cylinder(h=depth + 2 * wall_thickness, r=radius))
        self.box = empty_box(width, height, depth, wall_thickness).get()
        self.holes = [hole, right(width + (2*wall_thickness))(hole)]

        roof = (move_to_center_top(wall_thickness)(up(depth)(cube([width,height, wall_thickness]))))
        flaps = union()([intersection()(self.box, hole) for hole in self.holes])

        flaps = difference()(flaps, down(depth + wall_thickness)(roof))

        self.top = union()(roof, flaps)
        self.bottom = difference()(self.box, self.holes)

    def get_top(self):
        return self.top

    def get_bottom(self):
        return self.bottom

def main():
    width = 63.5
    height = 88
    depth = 20
    wall_thickness = 5.0

    object = card_holder(width, height, depth, wall_thickness)

    h = 20
    p = polyhedron(points=[[0,0,0],[2,0,0],[3,1,0],[-1,1,0],[0,0,h],[2,0,h],[3,1,h],[-1,1,h]],
                   faces =[[0,1,2,3],[4,5,1,0],[5,6,2,1],[6,7,3,2], [7,4,0,3],[7,6,5,4]])


    scad_render_to_file(object.get_top(), f"top_{width}x{height}mm.scad")
    scad_render_to_file(object.get_bottom(), f"bottom_{width}x{height}mm.scad")


    scad_render_to_file(p, f"filename.scad")
main()