# 2018-06-11
# InfoShare: day 05.
# task01 - przyklady list

# lista imion
names = ['pawel', 'michal', 'magda', 'ania', 'paulina']

print('Lista to: ', names)
print('Dlugosc listy names to: ', len(names))

first_element = names[0]
last_element = names[-1]
#wrong_element = names[784]

# dodawanie elementu na koniec listy
names.append('sebastian')
print('Lista to: ', names)
print('Ostatni element listy to: ', names[-1])

# count - liczy ile razy coś wystąpiło w obiekcie - tutaj w liście
name_to_find = 'przemek'
przemek_count = names.count(name_to_find)
print('Liczba osob o imieniu',name_to_find, przemek_count)

names.append('ania')
name_to_find = 'ania'
przemek_count = names.count(name_to_find)
print('Liczba osob o imieniu',name_to_find, przemek_count)

# wyszukajmy cos w liscie
idx = names.index(name_to_find)
print('index of', name_to_find, idx)

# wykorzystanie in
# sprawdż czy name_to_find znajduje się w liscie names
# jestli tak to wyświtl komunikat
if name_to_find in names:
    print('found :-)')
else:
    print('not found :-(')

# usuwanie z listy - przez slicy
second_row = names[1:3]
print(second_row)

# wyswietl kazdy element listy korzystajac petli
for name in names:
    print(name, end=' ')

print('')
for idx, name in enumerate(names):
    print(idx, name, sep=': ', end=' ')

# --------------
# dorzucenie imion z listy 2 do listy 1
additional_names = ['piotrek', 'kasia']

# doklei wszystkie elementy z listy2 do listy1
print(names)
names.extend(additional_names)
print(names)

# wykorzystanie operatorów matematycznych
additional_names2 = ['Janusz', 'Grazyna']
my_list = names + additional_names2  # jak extend
print(my_list)

# usuwanie z listy
name_to_remove = 'ania'
my_list.remove(name_to_remove)
print('after removal', my_list)

removed_item = my_list.pop()
print(removed_item)

# usuwanie
del my_list[2]

a = [1, 2, 3, 4, 5, 6]
a[0:1] = [] # zawsze musi być zakres, bo inaszej
a[0] = [] # przypisze puste