# 2018-06-18
# InfoShare: day 08.
# M. Ryś
#
# praca z plikami, pliki csv, with, tuple(krotka), dict(słownik)
# ------------------------------------------------------------------------------

# WYJĄTKI
try:
    print(test)
except NameError:
    print('Cos poszlo nie tak')

#
print('Jakis napis')

try:
    print('Jakis napis')
    print('Druga linia')
except IndentationError:
    print('Print był ze wcięciem ! Popraw to')

# syntax error
# try:
#     def mojasuperfunkcja()
#         print('test')
# except:
#     print('coś poszło nie tak')