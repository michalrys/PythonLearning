# 2018-07-02
# InfoShare: day 11.
# M. Ryś
# figury geometryczne
# ------------------------------------------------------------------------------
class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


a = 10
b = 20
prost = Rectangle(a, b)
print(f'Prostokąt: {prost.a}, {prost.b} -> pole: {prost.area()}')

kwadrat = Square(a)
print(f'Kwadrat: {kwadrat.a} -> pole: {kwadrat.area()}')
