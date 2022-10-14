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

    def thicken_floor(self, delta: float):
        self.box.thicken_floor(delta)

    def scad(self):
        pass