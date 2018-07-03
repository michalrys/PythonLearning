# 2018-07-02
# InfoShare: day 11.
# M. Ryś
# sprawdzenie czy obiekt jest instancją klasy
# sprawdzenie czy klasa jest podklasą innej klasy
# ------------------------------------------------------------------------------

class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
c = C()

print(isinstance(a,A))
print(issubclass(C, A))