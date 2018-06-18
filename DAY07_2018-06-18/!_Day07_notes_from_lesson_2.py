# 2018-06-18
# InfoShare: day 07.
# M. Ryś
#
# praca z plikami, pliki csv, with, tuple(krotka), dict(słownik)
# ------------------------------------------------------------------------------

# odczytanie danych z pliku
with open('test.txt', 'r+') as plik_01:
    plik_01_zawartosc = plik_01.read()

print(plik_01_zawartosc)

# zapis do pliku
nowe_dane_do_zapisu = 'A Jan ma psa2\n'

with open('test.txt', 'a') as plik_01:
    plik_01.write(nowe_dane_do_zapisu)

# odczytanie danych z pliku
with open('test.txt', 'r+') as plik_01:
    plik_01_zawartosc = plik_01.read()

print(plik_01_zawartosc)
