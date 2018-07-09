# 2018-07-08, M. Ryś
# EmployeeRegister - ver 1
# ------------------------------------------------------------------------------

class Worker:
    def __init__(self, name, lastname, salary):
        self.__name = name
        self.__lastname = lastname
        self.__salary = salary

    def status(self):
        print(self.__name, self.__lastname, self.__salary)

    @property
    def full_name(self):
        return f'{self.__lastname.capitalize()}, {self.__name.capitalize()}'

    def __str__(self):
        return self.__name + self.__lastname[0]

    def __repr__(self):
        return self.__str__()


jkowalski = Worker('jan', 'kowalski', 500)

print(jkowalski.full_name)