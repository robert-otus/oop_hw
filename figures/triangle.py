from figures.geometry import GeometricalFigure
from math import sqrt


class Triangle(GeometricalFigure):
    def triangle_perim(self, s1, s2, s3):
        perimeter = s1 + s2 + s3
        #print(f"The perimeter of the circle is {perimeter}")
        return perimeter

    def area_tri(self, st1, st2, st3):
        p = (st1 + st2 + st3) / 2
        area = sqrt(p * (p - st1) * (p - st2) * (p - st3))
        return area

t = Triangle("triangle", 3)
print(t.figure_name())
print(t.angle_quantity())
print(t.triangle_perim(11, 10, 6))
print(t.area_tri(11, 10, 6))
