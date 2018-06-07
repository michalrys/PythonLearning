# 2018-06-07
# Author: Michał Ryś
# InfoShare: day 03/04. Homework 03

# program obliczajacy liczbe liter i cyfr w stringu
# ------------------------------------------------------------------------------

# input data
sentence_user_input = input('Podaj zdanie: ')

# postprocessing input data
sentence = sentence_user_input

# amout of letters, numbers
sentence_letters_amount = 0
sentence_digits_amount = 0
sentence_other_amount = 0

# count letters
for char in sentence:
    if char.isalnum() and char.isdigit():
        sentence_digits_amount += 1
    elif char.isalnum():
        sentence_letters_amount += 1
    else:
        sentence_other_amount += 1

# print out
print(f'W podanym zdaniu: "{sentence}", jest:')

if sentence_digits_amount > 0:
    print(f'-> {sentence_digits_amount}x cyfr ')
if sentence_letters_amount > 0:
    print(f'-> {sentence_letters_amount}x liter ')
if sentence_other_amount > 0:
    print(f'-> {sentence_other_amount}x innych znaków ')
if sentence == '':
    print(f'-> nic nie ma :)')

