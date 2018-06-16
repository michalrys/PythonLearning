# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework

# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
# lista_b = [10,20,30,20,10,50,60,40,80,50,40]
# ------------------------------------------------------------------------------

# constants
MESSAGE_INPUTS = 'Twoja lista to: {list_input}'
MESSAGE_OUTPUTS = 'Lista z pozbawiona duplikatow: {lista_output}'
MESSAGE_SEPARATOR = 82 * '~'
MESSAGE_INFO = 'info: Lista -> zmiana na set -> zamiana na liste\n' \
               'set(): "(...)collection of distinct hashable objects. Common ' \
               'uses include membership testing, removing duplicates from a ' \
               'sequence, and computing mathematical operations (...)'

# input data
lista_b = [10, 20,30,20,10,50,60,40,80,50,40]
lista_b_bez_duplikwatow = list(set(lista_b))

# print out
print(MESSAGE_INPUTS.format(list_input=lista_b))
print(MESSAGE_OUTPUTS.format(lista_output=lista_b_bez_duplikwatow))
print(MESSAGE_SEPARATOR)
print(MESSAGE_INFO)
