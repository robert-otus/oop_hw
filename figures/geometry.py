

class GeometricalFigure:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def angle_quantity(self):
        if self.side > 0:
            return self.side
        else:
            return "This figure has no angles"

    def figure_name(self):
        return f"This is the {self.name}"






