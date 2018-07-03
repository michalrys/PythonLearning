# 2018-06-27
# InfoShare: day 10.
# M. Ryś
# OBIEKTY
# ------------------------------------------------------------------------------
class Complex(object):
    """Liczby zespolone"""
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other, self.imaginary * other)

    def __lt__(self, other):
        z = self.real ** 2 + self.imaginary ** 2
        y = other.real ** 2 + other.imaginary ** 2
        return z < y

    def __gt__(self, other):
        z = self.real ** 2 + self.imaginary ** 2
        y = other.real ** 2 + other.imaginary ** 2
        return z > y

a = Complex(1, 2)
b = Complex(4, 3)

print(str(a))
print(str(b))

print(a + b) # >> 5 + 5i
print(a * 4) # >> 1*4  + 4*3i

print(a > b) # 5 > 25
print(a < b) # 5 > 25