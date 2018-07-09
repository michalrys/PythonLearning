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
    caly_plik = plik.readlines()

delta_t_odczyt = time.time() - t0_odczyt
# print(caly_plik)

print('Czas odczytu = ', delta_t_odczyt)

print(caly_plik[0], end='')
print(caly_plik[1], end='')
print(caly_plik[2], end='')
print(caly_plik[3], end='')
print(caly_plik[4], end='')