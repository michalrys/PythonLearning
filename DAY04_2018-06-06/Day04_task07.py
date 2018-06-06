# 2018-06-06
# Michal Rys
# DAY 04: task07: z tablicy

text = 'Abracadabra'

replaced = '' # '' + 'X'

print(text)
print(replaced)

for char in text:
    print(char)

for idx, _ in enumerate(text):
    print(idx, text[idx])

# TODO: zamien co drugi znak na wielka litere
# TODO: kazdy string ma metode upper(), metoda replace(), count()

for idx, _ in enumerate(text):
    if idx % 2:
        replaced += text[idx]
    else:
        replaced += text[idx].upper()

print(f'{text} --> {replaced}')