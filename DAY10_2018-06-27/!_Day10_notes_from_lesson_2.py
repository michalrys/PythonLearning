# 2018-06-27
# InfoShare: day 10.
# M. Ryś
# OBIEKTY
# ------------------------------------------------------------------------------
class Car:
    def __init__(self, speed=0):
        self.speed = speed
    def increase_speed(self, value):
        self.speed += value
    def status(self):
        print(f'Predkość samochodu: {self.speed}')

# ------------------------------------------------------------------------------
car_1 = Car()

car_1.increase_speed(20)
car_1.status()

car_1.increase_speed(10)
car_1.status()
