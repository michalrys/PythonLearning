# 2018-06-06
# Michal Rys
# DAY 04: task02: 99 beers - w petli for

# TODO: na ekranie ma sie wyswietlac odliczanie
# TODO: od 99 do 0
# TODO: 'X beczek piwa na polce stalo, jedna spadla, Y zostalo'

beers = range(99, 0, -1)
# ver1:  message = '{} beczek piwa na polce stalo, jedna spadla {} zostalo'
# ver2:  message = '{beers_before} beczek piwa na polce stalo, jedna spadla ' \
# ver2:            '{beers_after} zostalo'

for beer in beers:
    # ver1:  print(message.format(beer, beer - 1))
    # ver2:  print(message.format(beers_before = beer, beers_after = beer - 1))
    message = f'{beer} beczek piwa na polce stalo, jedna spadla {beer - 1} zostalo'
    print(message)
