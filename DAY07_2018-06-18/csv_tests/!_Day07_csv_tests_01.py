# 2018-06-18
# InfoShare: day 07.
# M. Ryś
#
# testy z csv
# ------------------------------------------------------------------------------
import csv

print('Testy z csv.')

# aby były polskie znaki trzeba dodać encoding dla utf-8
with open("plik_csv_do_testow.csv", 'r', encoding='utf-8') as plik:
    spam_reader = csv.reader(plik, delimiter=',')
    linie = []
    for row in spam_reader:
        # print(row)
        linie.append(row)

# wpis 1, pozycja wpisu 2 = adres
print(linie[1][2])
