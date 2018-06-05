# 2018-06-05
# InfoShare: after day 03. Testy własne.
# M. Ryś

# napisz program, który sprawdzi czy liczba jest parzysta.
# liczba do sprawdzenia jest podawana przez użytkownika
# sprawdź czy podane dane to liczba.

# get user input data
value_user_input = input('Podaj liczbe: ')

# check input data
# check if first char is '-' or '+' or ''
if value_user_input[0] == '-':
    print('[info]: Liczba ma znak "%s"' % value_user_input[0])
    value_sign = value_user_input[0]
elif value_user_input[0] == '+':
    print('[info]: Liczba ma znak "%s"' % value_user_input[0])
    value_sign = ''
else:
    print('[info]: Liczba ma znak "+" ')
    value_sign = ''

# extract value without sign
value_without_sign = value_user_input[1:]

# check if value is digit
# if yes -> add sign to value and convert string to integer
if value_without_sign.isdigit():
    print(f'[info]: Dobrze. Podane dane to liczba.')
    value = value_sign + value_without_sign
    value = int(value)
else:
    print(f'[error]: Podane dane to nie jest liczba, albo nie jest to '
          f'liczba całkowita. Koniec programu.')
    exit(f'\n\n :-(')

# check if value is odd or even
if value % 2:
    print(f'[results]: Liczba {value} jest nieprzysta.')
else:
    print(f'[results]: Liczba {value} jest przysta.')

