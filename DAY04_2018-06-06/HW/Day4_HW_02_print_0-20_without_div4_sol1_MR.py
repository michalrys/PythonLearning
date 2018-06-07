# 2018-06-07
# Autor: Michał Ryś
# InfoShare: day 03/04. Homework 02

# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# continue
# ------------------------------------------------------------------------------

# list of constants
VALUE_LIMIT_UPPER = 20
VALUE_LIMIT_LOWER = 0
VALUE_DIVISOR = 4

# collection of numbers in list
values_without_numbers_div_by_divisor = []

# main program
for value in range(VALUE_LIMIT_LOWER + 1, VALUE_LIMIT_UPPER + 1):
    if value % VALUE_DIVISOR:
        values_without_numbers_div_by_divisor.append(str(value))
    else:
        continue

# print out
print(f'Liczby z zakresu od {VALUE_LIMIT_LOWER} do {VALUE_LIMIT_UPPER}', end='')
print(f', które są niepodzielne przez liczbę {VALUE_DIVISOR} to:')

for value_id, value in enumerate(values_without_numbers_div_by_divisor, start=1):
    if value == values_without_numbers_div_by_divisor[-1]:
        print(f'{value_id}: {value}.')
    else:
        print(f'{value_id}: {value},')
