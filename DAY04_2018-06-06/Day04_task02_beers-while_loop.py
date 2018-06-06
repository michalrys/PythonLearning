# 2018-06-06
# Michal Rys
# DAY 04: task02: 99 beers - w petli while

# TODO: na ekranie ma sie wyswietlac odliczanie
# TODO: od 99 do 0
# TODO: 'X beczek piwa na polce stalo, jedna spadla, Y zostalo'

MAX_BEERS = 99
MIN_BEERS = 0

current_amount_of_beers = MAX_BEERS
message = '{} beczek piwa na polce stalo, jedna spadla {} zostalo'

while current_amount_of_beers > MIN_BEERS:
    print(message.format(current_amount_of_beers, current_amount_of_beers - 1))
    current_amount_of_beers -= 1