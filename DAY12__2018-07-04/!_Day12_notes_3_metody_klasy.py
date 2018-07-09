# 2018-07-02, M. Ryś
# InfoShare: day 12.
#
# ------------------------------------------------------------------------------
class Car:
    max_speed = 300

    @classmethod
    def status(cls):
        print('Istnieje')
        print(Car.max_speed)

    def __init__(self, speed=10):
        self.speed = speed


audi = Car()

audi.status()
Car.status()


