# 2018-06-06
# Michal Rys
# DAY 04: task05 podejście 3

# TODO: zamien co drugi znak na wielka litere
# TODO: kazdy string ma metode upper(), metoda replace(), count()

text = 'Abracadabra'

text_new = ''

text_length = len(text)

print(text_length)

for char in range(0, text_length, 2):
    text_new += text[char].upper()
    text_new += text[char + 1].upper()

print('{text} --> {text_new}')


# a = range(10)
# b = range(33, 46)
#
# for el_a, el_b in zip(a, b):
#     print(el_a, el_b)