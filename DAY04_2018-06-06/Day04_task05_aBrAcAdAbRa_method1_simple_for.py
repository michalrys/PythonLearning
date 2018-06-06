# 2018-06-06
# Michal Rys
# DAY 04: task05 podejście 1

# TODO: zamien co drugi znak na wielka litere
# TODO: kazdy string ma metode upper(), metoda replace(), count()

text = 'Abracadabra'

text_new = ''
position = 1

for char in text:
    if position == 1:
        text_new = text_new + char.lower()
    elif position == 2:
        text_new = text_new + char.upper()

    if position == 1:
        position += 1
    else:
        position = 1

print(f'{text} --> {text_new}')

# for ifx, char in enumerate(text):
#     print(idx, text[idx])