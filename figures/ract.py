from figures.geometry import GeometricalFigure


class Ractangular(GeometricalFigure):
    def ract_perim(self, s1, s2):
        perimeter = 2 * s1 + 2 * s2
        #print(f"The perimeter of the ractangular is {perimeter}")
        return perimeter

    def area_ract(self, st1, st2):
        area = st1 * st2
        return area

rt = Ractangular("ractangular", 4)
print(rt.figure_name())
print(rt.angle_quantity())
rt.ract_perim(3, 2)
rt.area_ract(3, 2)
