a = {'imie': 'jan', 'nazwisko': 'nowak', 'wiek': '23', 'oczy':'niebieskie'}

b = list(a.keys())[1:]

# b = a.keys()

print(b)
for klucz in b:
    print(a[klucz])

# for i in a[1:]:
#     print(i)