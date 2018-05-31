#  Created in: 2018-05-30
# Finished in: 2018-05-31
#      Author: Michał Ryś
#     Version: 1.00
# -----------------------
# ZADANIE1
#
# output:
# 'Arek woli psy, a najbardziej boksery'
#
# nie wolno dostarczyc znakow z zewnatrz
# mozna dowolnie przeksztalcac

x = "Ala ma kota, kot ma Ale"

# rozwiazanie metodą 1 #########################################################
print('\n[info]:\t', 'Metoda rozwiazania 1: przez replace')

# użycie replace
output_solution_1 = x.replace('Ala ma kota, kot ma Ale',
                              'Arek woli psy, a najbardziej boksery')

# podsumowanie: wydrukowanie inputu, outputu
print('[input]:\t', x)
print('[output]:\t', output_solution_1)
print('-----------------------------------------------------------------', '\n')

# rozwiazanie metoda 2 #########################################################
# modyfikacja w kodowaniu kolejnych liter, dopisanie znakow do stringa
print('[info]:\t', 'Metoda rozwiazania 2: zmiana liter przez przesuniecie '
                    'sie w tablicy unicode\n')

# okreslenie ile jest znakow w outpucie (trzeba by to policzyć ręcznie, ale
#                                        robie to automatycznie)
output_sentence = 'Arek woli psy, a najbardziej boksery'
output_sentence_length = len(output_sentence)
# >> 36
print('[info]: Ilosc znakow: ', output_sentence_length, ': ', output_sentence)

# okreslenie ile jest znakow w inpucie
# input_sentence jest za krotkie, zwiekszam dlugosc x2
#     (mozna zapisać x+x, albo  2*x. Można to zautomatyzować na przyszłość
#      --> pętla: tak długo dodawaj +x aż długość output > długosć input,
#      a potem przytnij do długości input)
input_sentence = x+x
# input_sentence jest za dlugie

# wyrownanie dlugosci
input_sentence = input_sentence[:output_sentence_length]
input_sentence_length = len(input_sentence)
print('[info]: Ilosc znakow: ', input_sentence_length, ': ', input_sentence)

# określenie wartości o jaką trzeba się przeusnąć w kodowaniu unicode aby
# przerobic każdą literę zdania wejsciowego na odpowiednią literę zdania
# wyjściowego
#     ( można by zrobić to w jednej pętli i krócej, na cele sprawdzenia
#       porównuje każdą literę i określam offset dla wartości unicode litery)
#     ( ! sprawdzić prostsze porównania)
j_temp = 0
offset_all = []
for i in input_sentence:
    # użyłem pętli, bo ręczne sprawdzanie jest bez sennsu
    # ord --> zwaraca nr unicode z litery,
    # chr --> zwaraca litere z nr unicode (na potem).
    letter_current = i
    letter_current_unicode_number = ord(letter_current)
    letter_target = output_sentence[j_temp]
    letter_target_unicode_number = ord(letter_target)
    offset_for_letter_current = \
        letter_target_unicode_number - letter_current_unicode_number

    # robie liste z offsetami, które potem dodam
    offset_all.append(offset_for_letter_current)

    print('[info]: Aby z litery: ', letter_current, ' zrobic litere: ',
          letter_target, ' trzeba przesunac sie w unicode o wartosc: ',
          offset_for_letter_current)
    j_temp += 1

# tworze wyjściowy y bazując na znakach unicode znaków łańcucha input
# poprzez dodanie do nich offestu
#     (można by to zrobić we wcześniejszej pętli, i skrócić cały kod,
#      ale zrobiłem sobie tak :)
y = ''
j_temp = 0
for i in input_sentence:
    letter_current = i
    letter_current_unicode_number = ord(letter_current)
    letter_current_new_unicode_number = letter_current_unicode_number + \
                                        offset_all[j_temp]
    letter_current_new = chr(letter_current_new_unicode_number)
    y = y + letter_current_new
    j_temp += 1

# podsumowanie metody 2: wydrukowanie inputu, outputu
print('\n[input]:\t', x)
print('[output]:\t', y)
print('-----------------------------------------------------------------', '\n')

# rozwiazanie metodą 3 #########################################################
# wieksza automatyzacja
print('\n[info]:\t', 'Metoda rozwiazania 3: wieksza automatyzacja\n')

# jeszcze raz przypisanie danych wejsciowych do obróbki
input_sentence = x
output_sentence = y
# ------ tylko dla testów (zakomentuj dwie wczesniejsze linijki) ----
# input_sentence = 'Ala lubi jabłka'
# x = input_sentence
# output_sentence = 'A Janusz ma nóż'
# ------ tylko dla testów ----

# okreslenie dlugosci
input_sentence_length = len(input_sentence)
output_sentence_length = len(output_sentence)

# pokazanie inputu
print('[info]:\t', 'Tekst input: "', sep='', end='')
print(input_sentence, sep='', end='')
print('", ma tyle znaków: ', sep='', end='')
print(input_sentence_length, sep='', end='\n')

# pokazanie outputu
print('[info]:\t', 'Tekst output: "', sep='', end='')
print(output_sentence, sep='', end='')
print('", ma tyle znaków: ', sep='', end='')
print(output_sentence_length, sep='', end='\n')


# automatyczne wydłuzenie / skrócenie input_sentence
#     (!na potem: najlepiej przerobic to na funkcje)
if input_sentence_length == output_sentence_length:
    print('[info]: Dlugosc tekstu wejsciowego jest w sam raz :).')
elif input_sentence_length < output_sentence_length:
    print('[info]: Tekst wejsciowy trzeba wydluzyc.')
    # wydluzenie automatyczne i docięcie
    input_multi = (output_sentence_length // input_sentence_length) + 1
    input_sentence = input_multi * input_sentence
    input_sentence = input_sentence[:output_sentence_length]

    # wynik wydluzenia (!na potem: wyswietlanie info przerobic na funkcje)
    input_sentence_length = len(input_sentence)
    print('[info]:\t', 'Wydluzony tekst wejsciowy: "', sep='', end='')
    print(input_sentence, sep='', end='')
    print('", ma tyle znaków: ', sep='', end='')
    print(input_sentence_length, sep='', end='\n')

elif input_sentence_length > output_sentence_length:
    print('[info]: Tekst wejsciowy trzeba skrocic.')
    # skrocenie automatyczne
    input_sentence = input_sentence[:output_sentence_length]

    # wynik skrocenia
    input_sentence_length = len(input_sentence)
    print('[info]:\t', 'Skrocony tekst wejsciowy: "', sep='', end='')
    print(input_sentence, sep='', end='')
    print('", ma tyle znaków: ', sep='', end='')
    print(input_sentence_length, sep='', end='\n')

# krotsze porownanie znakow i przerobka iteracyjna
y = ''
output_sentence_char_position = 0
for i in input_sentence:
    j = output_sentence[output_sentence_char_position]
    while i != j:
        if i > j:
            # przesun sie w lewo w tablicy unicode
            i = chr(   ( ord(i) ) - 1  )
        elif i < j:
            # przesun sie w prawo w tablicy unicode
            i = chr(   ( ord(i) ) + 1  )
    y = y + i
    output_sentence_char_position += 1
# (!na potem: można sprawdzić czas szukania,
#             przerobienie na funkcje?: wej=input,output wyj=output)

# podsumowanie metody 3: wydrukowanie inputu, outputu
print('\n[input]:\t', x)
print('[output]:\t', y)
print('-----------------------------------------------------------------', '\n')
