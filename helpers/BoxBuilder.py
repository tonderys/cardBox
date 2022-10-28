from solid import *

from parametricBox.interior.Interior import *

from parametricBox.WithJoints import *
from parametricBox.WithVerticalHoles import *
from parametricBox.WithHorizontalHole import *
from parametricBox.WithRoundedCorners import *

class BoxBuilder:
    def __init__(self, inner: Interior, filename):
        self.object = inner
        self.filename = filename

    def withJoints(self):
        self.object = WithJoints(self.object)
        return self

    def withVerticalHoles(self):
        self.object = WithVerticalHoles(self.object)
        return self

    def withHorizontalHole(self):
        self.object = WithHorizontalHole(self.object)
        return self

    def build(self):
        self.object = WithRoundedCorners(self.object)
        scad_render_to_file(self.object.scad(), self.filename)
