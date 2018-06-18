# 2018-06-18
# InfoShare: day 07.
# M. Ryś
#
# praca z plikami, pliki csv, with, tuple(krotka), dict(słownik)
# ------------------------------------------------------------------------------

# zapis daty do pliku
with open("test.txt", 'w') as plik:
    plik.write('Dzisiejsza data: 2018-06-18.')

# odczyt
with open("test.txt", 'r+') as plik:
    linijka_1 = plik.readline()
    pozycja = plik.tell()
    plik.seek(-5, 2)
    pozycja = plik.tell()
    wczytaj_wszystko = plik.read()

linijka_1_length = len(linijka_1)

print('Linijka 1: ', linijka_1)
print('Linijka 1 długość: ', linijka_1_length)
print('Pozycja kursora: ', pozycja)
print('Wczytanie wszystkiego: ', wczytaj_wszystko)


