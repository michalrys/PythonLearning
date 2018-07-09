# 2018-06-18
# InfoShare: day 07.
# M. Ryś
#
# praca z plikami, pliki csv, with, tuple(krotka), dict(słownik)
# ------------------------------------------------------------------------------
import time

t0_odczyt = time.time()
# odczyt
with open("data_test.neu", 'r') as plik:
    caly_plik = plik.read()

delta_t_odczyt = time.time() - t0_odczyt
# print(caly_plik)


t0_zapis = time.time()
with open("data_test_ponowny_zapis.neu", 'w') as plik:
    plik.write(caly_plik)

print('OK, zapisano')
delta_t_zapis = time.time() - t0_zapis

print('Czas odczytu = ', delta_t_odczyt)
print('Czas zapisu = ', delta_t_zapis)