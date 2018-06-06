# 2018-06-04
# Michal Rys
# DAY 03: task02

# TODO: napisz program, który sprawdzi czy liczba jest parzysta.
# TODO: liczba do sprawdzenia jest podawana przez użytkownika
# TODO: sprawdź czy podane dane to liczba.

value = input('Podaj liczbe: ')

if value.isdigit():
    value = int(value)
    if value % 2:
        print(f'Podana liczba: {value} jest nieprzysta')
    else:
        print(f'Podana liczba: {value} jest przysta')
else:
    print(f'Podane dane: {value} nie sa liczba. Przerywam wykonanie kodu.')
# sprawdź ten kod : http://pythontutor.com/visualize.html#mode=edit

# jak zrobić zeby -34 traktował jako liczbę
