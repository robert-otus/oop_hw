from square import Square
from ract import Ractangular
from triangle import Triangle
from circle import Circle


class AreaSum:
    def add_square(self):
        n = input("Enter the name of figure: ")
        if n == "triangle":
            sum = Circle("circle", 0).area_cir(3) + Triangle("triangle", 3).area_tri(2, 3, 4)
            print(sum)
        elif n == "ractangular":
            sum = Circle("circle", 0).area_cir(3) + Ractangular("ractangular", 4).area_ract(2, 3)
            print(sum)
        elif n == "square":
            sum = Circle("circle", 0).area_cir(3) + Square("square", 4).area_sq(2)
            print(sum)
        elif n == "circle":
            sum = Circle("circle", 0).area_cir(3) + 0
            print(sum)
        else:
            print("Error. Not a valid class")


a = AreaSum()
a.add_square()
