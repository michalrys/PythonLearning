# 2018-06-04
# Michal Rys
# DAY 03: task01

# 1 - podaj imie użytkownika (input)
# 2.0 - jeśli imie podane przez użytkownika == Piotr ?
# 2.1 - wyświetl tekst powitalny
# 2.2 - w przeciwnym razie --> wyświetl tekst: "Hej, poklikasz...?"
ADMIN_USERNAME = 'Piotr'

input_user_name = input('Podaj imie: ')

# obróbka danych wejściowych
# bo jak ktos wpisze PIOTR
user_name = input_user_name.lower()
# a teraz daje pierwsza dużą
user_name = user_name.capitalize()

#               było tutaj 'Piotr' --> RMB --> Refactor -> Exctract -> Constant
if user_name == ADMIN_USERNAME:
    # można komunikaty wyrzucić też do stałych = czytelniejsze, łatw. do rozsz.
    print(f'Witaj {user_name}')
else:
    print('Hej, poklikasz... ?')

# dobra praktyka:  COMMIT EARLY, COMMIT OFTEN
# @TODO: some commentm