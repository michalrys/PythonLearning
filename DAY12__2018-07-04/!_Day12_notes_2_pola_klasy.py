# 2018-07-02, M. Ryś
# InfoShare: day 12.
#
# ------------------------------------------------------------------------------
class Car:
    max_speed = 200

    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed  # przesłoniło się


audi = Car(30, 300)

Car.max_speed = 400
print(audi.speed, audi.max_speed, Car.max_speed)


