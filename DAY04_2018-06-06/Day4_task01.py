# 2018-06-06
# Michal Rys
# DAY 04: task01: while loop

# TODO: pobierz od uzytkownika dwie liczby
# TODO: w petli while sprawdz czy a > b
# TODO: wyswietl na ekranie aktualna wartosc liczby a
# TODO: jesli tak, to a zmniejsz o 1

# input data from user
a = input('Podaj liczbe a= ')
b = input('Podaj liczbe b= ')

# check input data, correction
a = int(a)
b = int(b)

# check if a > b
while a > b:
    print(f'Liczba a = {a}')
    a -= 1

