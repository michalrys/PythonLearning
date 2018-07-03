# 2018-07-02
# InfoShare: day 11.
# M. Ryś
# figury geometryczne
# ------------------------------------------------------------------------------
class Figure:
    def __init__(self):
        self.sides = []
    def area(self):
        pass

    def perimeter(self):
        sum_all = 0
        for side in self.sides:
            sum_all += side
        return sum_all

class Triangle(Figure):
    def __init__(self):
        super().__init__()
        self.height = float(0)
    def area(self):
        return 0.5 * self.sides[0] * self.height

class Rectangle(Figure):
    def area(self):
        pass

    def perimeter(self):
        sum_all = 0
        sum_all = 2 * self.sides[0] + 2 * self.sides[1]
        return sum_all

# ------------------------------------------------------------------------------
t = Triangle()
t.sides = [1,2,3]
t.height = 10

r = Rectangle()
r.sides = [2, 4]

print(f' Trojkąt: boki={t.sides}, wysokość={t.height}, ma pole {t.perimeter()}')
print(f' Prostokąt: {r.sides}, ma pole {r.perimeter()}')



