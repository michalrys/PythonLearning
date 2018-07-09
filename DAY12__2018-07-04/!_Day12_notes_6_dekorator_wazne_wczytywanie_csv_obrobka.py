# 2018-07-02, M. Ryś
# InfoShare: day 12.
#
# ------------------------------------------------------------------------------

class CSVBeatufuler:
    def __init__(self, path):
        with open(path, 'r') as file:
            self.__content = file.readlines()

    @property
    def headers(self):
        return self.__content[0].split(',')

    @property
    def content(self):
        linie = []
        for l in self.__content[1:]:
            linie.append(l.split(','))
        return linie

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            line = ', '.join(value)
            self.__content.append(line)


cb = CSVBeatufuler('test.csv')
print(cb.headers)
print(cb.content)

cb.content = ['Michal', 'Nowak']
print(cb.content)



# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return str(self.__name).capitalize()
#
#     def print_name(self):
#         return str(self.__name)
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
# f = Person('jaś')
#
# print(f.print_name())
# print(f.name)
# print(f.print_name())
#
# f.name = 'małgosia'
#
# print(f.print_name())
# print(f.name)
# print(f.print_name())