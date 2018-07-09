# 2018-07-02, M. Ryś
# InfoShare: day 12.
#
# ------------------------------------------------------------------------------

class Car:
    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print(self.__name)


audi = Car('Michał')

audi.print_name()

print(audi.__dict__)
print(audi._Car__name)
print('Użycie dir()')
print(dir(Car))

