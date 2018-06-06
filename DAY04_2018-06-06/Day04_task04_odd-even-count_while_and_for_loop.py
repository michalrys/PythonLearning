# 2018-06-06
# Michal Rys
# DAY 04: task04. policzenie liczb parzystych / nieparzystych

# TODO: pobierz od uzytkownika liczbe, ktora bedzie gorna granica zakresu
# TODO: dolny zakres 0
# TODO: w danym zakresi zlicz liczby parzyste i niepaprzyste

MIN_VALUE = 0

max_value = int(input('Podaj liczbe gornego zakresu = '))

# solve for while
current_value = max_value

# ilosc liczb parzystych = even, odd -> nieparzystych
amount_of_even = 0
amount_of_odd = 0

print('Wyniki dla petli WHILE: ')

while current_value > MIN_VALUE:
    if current_value % 2:
        print(f'{current_value} --> nieparzysta')
        amount_of_odd += 1
    else:
        print(f'{current_value} --> parzysta')
        amount_of_even += 1
    current_value -= 1

# summerize
print(f'Ilosc parzystych = {amount_of_odd}, ilosc nieparzystych {amount_of_even}')
print('-----------------------------------------------------------------------')
#-------------------------------------------------------------------------------
print('\n')
# w petli for
amount_of_odd_in_for_loop = 0
amount_of_even_in_for_loop = 0

print('Wyniki dla petli FOR: ')

for current_value in range(1, max_value + 1, 1):
    if current_value % 2:
        print(f'{current_value} --> nieparzysta')
        amount_of_odd_in_for_loop += 1
    else:
        print(f'{current_value} --> parzysta')
        amount_of_even_in_for_loop += 1

# summerize2
print(f'Ilosc parzystych = {amount_of_even_in_for_loop}, '
      f'ilosc nieparzystych {amount_of_odd_in_for_loop}')
print('-----------------------------------------------------------------------')
