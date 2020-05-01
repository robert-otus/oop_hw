from figures.geometry import GeometricalFigure


class Square(GeometricalFigure):
    def square_perim(self, size):
        perimeter = size * 4
        return perimeter

    def area_sq(self, s):
        area = s * s
        return area

s = Square("square", 4)
print(s.figure_name())
# print(s.angle_quantity())
# s.square_perim(3)
# s.area_sq(3)

