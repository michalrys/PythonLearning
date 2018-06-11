# 2018-06-11
# InfoShare: day 05.
# task03 - listy zadanie z duplikatami

# iterując się po kążdym elemencie z listy duplicates
# dodaj elementy do listy without duplicates tylko jeżeli
# już się w niej nie znajduje (lista ma nie zawierać duplikatów)

duplicates = [1, 2, 3, 1, 4, 7, 7, 1, 2, 3, 3]

without_duplicates = []

for element in duplicates:
    if element in without_duplicates:
        continue
    else:
        without_duplicates.append(element)

print(duplicates)
print(without_duplicates)

# if element not in without_duplicates:
# not if element in without_duplicates:
