# 2018-06-05
# InfoShare: after day 03. Testy własne.
# M. Ryś

# 1 - podaj imie uĹĽytkownika (input)
# 2.0 - jeĹ›li imie podane przez uĹĽytkownika == Piotr ?
# 2.1 - wyĹ›wietl tekst powitalny
# 2.2 - w przeciwnym razie --> wyĹ›wietl tekst: "Hej, poklikasz...?"

# constants
USER_NAME_SPECIAL = 'Piotr'
question_number_for_interruption = 3

# regular expression
import re

# error,     id, descriptin
error_code = 999
question_iteration = 1

# promt for name until input is correct
while error_code != 0:
    # get input data from user
    user_name_input = input('Podaj imie: ')

    # make all letters lowercase and capitalize first letter
    user_name = user_name_input.lower().capitalize()

    # check for input error
    if question_iteration == question_number_for_interruption:
        # interruption
        error_code = 0
        print(f'[info]: Podałeś {question_iteration} razy błędne imię. '
              f'Przerywam program.')
        exit(f'\n[exit_info]: Błąd. {question_iteration} x razy podano błędnie imie.')
    elif ' ' in user_name:
        # error code 1: no empty space is allowed
        error_code = 1
        print(f'[info]: Błędne dane. Podałeś imię: "{user_name}" z '
              f'niedozwolonym znakiem " ". Popraw to.')
    # składnia: \d = any digit character w user_name
    elif re.findall('\d', user_name):
        # error code 2: no numbers are allowed
        error_code = 2
        print(f'[info]: Błędne dane. Podałeś imię: "{user_name}" z '
              f'niedozwolonym znakiem - w imieniu nie mogą występować '
              f'liczby. Popraw to.')
    elif user_name == "":
        # error code 3: no empty name is allowed
        error_code = 3
        print(f'[info]: Błędne dane. Podałeś puste imię. Popraw to.')
    elif re.findall('[aąeęioóuyAEIOUY]', user_name) == []:
        # error code 4: lack of vowel is not allowed
        error_code = 4
        print(f'[info]: Błędne dane. Podałeś imię: "{user_name}", '
              f'które nie ma ani jednej samogłoski. To jest niemożliwe. '
              f'Popraw to.')
    else:
        # no error
        error_code = 0
    question_iteration += 1

# name check
if user_name_input == USER_NAME_SPECIAL:
    print(f'Witaj adminie {user_name}! Podałeś prawidłowe imię. Jesteś w trybie'
          f' boss-mode')
else:
    print('%s poklikasz ?' % user_name)