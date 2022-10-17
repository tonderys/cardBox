class Box():
    def get_width(self) -> float:
        return self.box.get_width()

    def get_height(self) -> float:
        return self.box.get_height()

    def get_depth(self) -> float:
        return self.box.get_depth()

    def get_wall_x(self) -> float:
        return self.box.get_wall_x()

    def get_wall_y(self) -> float:
        return self.box.get_wall_y()

    def get_floor(self) -> float:
        return self.box.get_floor()

    def log(self) -> str:
        return self.box.log() + "\n" + \
               f"created {type(self).__name__} " + \
               f"with dimensions {self.get_width()}(w) x {self.get_height()}(h) x {self.get_depth()}(d) " + \
               f"and walls {self.get_wall_x()}(x) {self.get_wall_y()}(y) {self.get_floor()}(floor)"

    def scad(self):
        pass