# options to choose
CB_OPTIONS_KEY = []

for option in range(10):
    CB_OPTIONS_KEY.append(option)

print(CB_OPTIONS_KEY)
print(type(CB_OPTIONS_KEY[5]))


# options to choose - na slownikach
CB_OPTIONS = {}
CB_OPTIONS[CB_OPTIONS_KEY[1]] = 'dodaj imię'
CB_OPTIONS[CB_OPTIONS_KEY[2]] = 'usuń imię'
CB_OPTIONS[CB_OPTIONS_KEY[3]] = 'sprawdź czy imię jest w bazie'
CB_OPTIONS[CB_OPTIONS_KEY[4]] = 'wyświetl całą książkę adresową'
CB_OPTIONS[CB_OPTIONS_KEY[5]] = 'zamknij program'

print(CB_OPTIONS)
print(f'[{CB_OPTIONS_KEY[1]}]: {CB_OPTIONS[CB_OPTIONS_KEY[1]]}.')
print(f'[{CB_OPTIONS_KEY[2]}]: {CB_OPTIONS[CB_OPTIONS_KEY[2]]}.')
print(f'[{CB_OPTIONS_KEY[3]}]: {CB_OPTIONS[CB_OPTIONS_KEY[3]]}.')
print(f'[{CB_OPTIONS_KEY[4]}]: {CB_OPTIONS[CB_OPTIONS_KEY[4]]}.')
print(f'[{CB_OPTIONS_KEY[5]}]: {CB_OPTIONS[CB_OPTIONS_KEY[5]]}.')
