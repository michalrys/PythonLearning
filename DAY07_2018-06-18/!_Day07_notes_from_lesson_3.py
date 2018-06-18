# 2018-06-18
# InfoShare: day 07.
# M. Ryś
#
# praca z plikami, pliki csv, with, tuple(krotka), dict(słownik)
# ------------------------------------------------------------------------------

# zapis daty do pliku
with open("test.txt", 'w') as plik:
    plik.write('Dzisiejsza data: 2018-06-18.\nLekcja nr 7\nKrakow')

# odczyt pliku
with open("test.txt", 'r') as plik:
    plik_zawartosc_cala = plik.read()

# odczyt pliku
with open("test.txt", 'r') as plik:
    plik_zawartosc_linijka = plik.readline()

# odczyt pliku
with open("test.txt", 'r') as plik:
    plik_zawartosc_linijki = plik.readlines()

# wyświelenie pliku
print(plik_zawartosc_cala)
print(82 * '-')

print(plik_zawartosc_linijka)
print(82 * '-')

print(plik_zawartosc_linijki)
print(82 * '-')

