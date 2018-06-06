# 2018-06-06
# InfoShare: day 04. Notatki z zajęć.
# M. Ryś

# przede wszystkim listy oraz pętle

# schemat blokowy - oznaczenie pętli
# pętla while

# nie ma pętli do - while :)

# funkcja range()
range_utworzenie_1 = range(3)
print(f'Utworzenie range metoda1: {range_utworzenie_1}')

#                       start, stop, (domyslny krok 1)
range_utworzenie_2 = range(4,8)
print(f'Utworzenie range metoda2: {range_utworzenie_2}')

# krok musi byc calkowity, nie moze byc floatem
#                        start, stop, krok
range_utworzenie_3 = range(0,10,2)
print(f'Utworzenie range metoda3: {range_utworzenie_3}')

# pętla for
for i in range(10,-10,-1):
    print(f'i = {i} ,',end='')

# na zapętlenie
# ctrl + c

# ------------------------------------------------------------------------------
# enumerate()
# zip()

# enumerate() --> odpowiednik
# for (indeks, element) in enumerate(kolekcja):
# daje
print('')

pory_roku = ['lato', 'jesien', 'zima', 'wiosna']
for (i, i_value) in enumerate(pory_roku):
    print(f'i = {i} = {i_value}, ',end='')


# enumerate, przyklad uzycia
# list(enumerate(['test1', 'test2']))
# list(enumerate(['test1', 'test2'],2))

# zip() - uzycie
# list(zip('abcde','12345','ABCDE'))