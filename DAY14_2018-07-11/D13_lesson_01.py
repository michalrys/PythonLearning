# 2018-07-11, M. Ryś
# InfoShare day 13 - środa
# github i git, argumenty programów, modyfikowanie zdjęć, krótkie podsumowanie
# sys.argv
# ------------------------------------------------------------------------------

import sys
import os

print(sys.argv)


def add(a, b):
    return a + b


def multi(a, b):
    return a * b


a = int(sys.argv[1])
b = int(sys.argv[2])

print(add(a, b))
print(multi(a, b))
