# 2018-06-04
# InfoShare: day 03. Notatki z zajęć.
# M. Ryś

# pętle if
a = 2

if a == 1:
    print('yupi')
elif a == 4:
    print('a wynosi 4')
else:
    print('oh no')

# Algorytm szukania nazwiska w książce telefonicznej
nazwisko = 'Test'
nazwiska_lista = ['Ala', 'Test']

# print(f'{nazwiska_lista[0]}')

# można wykorzystać do sprawdzenia nazwiska czy jest w książce telefonicznej
# - nazwiska_lista: książka, - nazwisko: aktualne nazwisko.
if nazwisko in nazwiska_lista:
    print(f'Nazwisko {nazwisko} jest w {nazwiska_lista}')


# gdy znajdzie spełnienie warunku to przerywa
a = 'koniec petli'
if a == 'koniec petli':
    print('Koniec petli - zakonczono na sprawdzeniu 1.')
elif a == 'koniec petli':
    print('Koniec petli - zakonczono na sprawdzeniu 2.')

#-------------------------------------------------------------------------------
# tablice logiczne
# AND, OR

# typ bool
print(f'Sprawdzenie bool(3) to {bool(3)}')
print(f'Sprawdzenie bool(0) to {bool(0)}')
print(f'Sprawdzenie bool("Napis") to {bool("Napis")}')
print(f'Sprawdzenie bool("") to {bool("")}')

# bool jest = true gdy jest nie pusty.

#------------- ZEN of python
# import this
# PEP 8 --> pep-0008

# if (first_value and second_value
#     third_value == 0):
#     do_something()
