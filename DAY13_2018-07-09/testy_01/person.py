# 2018-07-09, M. Ryś
# InfoShare: day 13.
# tests - plik ktory bedzie testowayn
# ------------------------------------------------------------------------------


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.surname}, {self.name}'

