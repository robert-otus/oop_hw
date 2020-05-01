from figures.geometry import GeometricalFigure


class Circle(GeometricalFigure):
    def circle_perim(self, rad):
        pi = 3.14
        circ = 2 * pi * rad
        #print(f"The circumference of the circle is {circ}")
        return circ

    def area_cir(self, r):
        pi = 3.14
        area = pi * (r ** 2)
        return area


c = Circle("circle", 0)
print(c.figure_name())
print(c.angle_quantity())
c.circle_perim(5)
c.area_cir(5)

