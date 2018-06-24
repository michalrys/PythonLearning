# 2018-06-11
# InfoShare: day 05.
# task01 - listy złożone, zagnieżdżone = nested list

import copy

chemia = ['proszek do prania',
          'mydlo',
          'pasta do zebow']

warzywa = ['burak',
           'marchewka',
           'pietruszka',
           'seler']

zakupy_czerwiec = [chemia, warzywa]
print('VI: ', zakupy_czerwiec)

zakupy_lipiec = zakupy_czerwiec.copy()
print('VII: ', zakupy_lipiec)

# dodanie warzywa do listy, ale tylko w lipcu
#
# tutaj kopia jest płytka. nie działa - listy zakupy_czerwiec i zakupy_lipiec
# będą takie same. nie o to nam chodziło.
# zakupy_lipiec = zakupy_czerwiec.copy()
zakupy_lipiec[1].append('ogorek')
print(zakupy_czerwiec)
print(zakupy_lipiec)
#
# # kopia glęboka, przez copy.deepcopy
# zakupy_lipiec = copy.deepcopy(zakupy_czerwiec)
# zakupy_lipiec[1].append('ogorek')
# print('')
# print('VI: po', zakupy_czerwiec)
# print('VII: po', zakupy_lipiec)
#
# print(dir())
# # copy --> shallow copy - kopia płytka. dobre dla typów prostych
# # dla typów złożonych --> deepcopy:
# # deep copy tworzy nowy obszar w pamięci, gdzie kopiuje dane
# #
# # uważać na rozmowach kwal.
#
# print('--------------------')
# print('--------------------')
# # ------------------------------------------------------------------------------
# # jak przeliterować się po nested list
# for kategoria_zakupow in zakupy_lipiec:
#     for towar in kategoria_zakupow:
#         print(towar)
#     print()
#
# # test
# # odwolania do listy w liscie
# a[1:3]
# a[1:3][0]
# a[1:3][0][0]
# a[1][2]
#
# a[0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1][0:1]
# a[0][0]

