from solid import *

from parametricBox.interior.Interior import *

from parametricBox.PlainBox import *
from parametricBox.WithJoints import *
from parametricBox.WithVerticalHoles import *
from parametricBox.WithHorizontalHole import *
from parametricBox.WithRoundedCorners import *

separator = "\n---------------------------------------------------------\n"

class BoxBuilder:
    def __init__(self, inner: Interior, filename):
        self.object = PlainBox(inner)
        self.filename = filename

    def withRoof(self, roof):
        self.object.get_roof = roof
        return self

    def withJoints(self):
        self.object = WithJoints(self.object)
        self.log = self.object.log() + "\n"
        return self

    def withVerticalHoles(self):
        self.object = WithVerticalHoles(self.object)
        self.log = self.object.log() + "\n"
        return self

    def withHorizontalHole(self):
        self.object = WithHorizontalHole(self.object)
        self.log = self.object.log() + "\n"
        return self

    def build(self):
        self.object = WithRoundedCorners(self.object)
        print(f"{separator}{self.log}saved as \"{self.filename}\"{separator}")
        scad_render_to_file(self.object.scad(), self.filename)
