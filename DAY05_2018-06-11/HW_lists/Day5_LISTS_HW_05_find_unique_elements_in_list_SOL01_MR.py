# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework 03

# program znajdujacy wartosci, ktre wystepuja tylko raz
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
# ------------------------------------------------------------------------------

# constants
MESSAGE_INPUTS = 'Twoja lista to: {list_input}'
MESSAGE_OUTPUTS = 'Lista z unikalnymi elementami to: {lista_output}'
MESSAGE_SEPARATOR = 82 * '~'

# input data
lista_a = [10,20,30,20,10,50,60,40,80,50,40]

lista_a_unique = []
# do
for element in lista_a:
    if not lista_a.count(element) > 1:
        lista_a_unique.append(element)

# print out
print(MESSAGE_INPUTS.format(list_input=lista_a))
print(MESSAGE_OUTPUTS.format(lista_output=lista_a_unique))

# ------------------------------------------------------------------------------
# method 2: use of function
print(MESSAGE_SEPARATOR)

def get_unique_elements(list_input: list) -> list:
    """Get unique list of elements from list.

    :param list list_input: user input list.
    :return: list with unique elements.
    """
    list_of_unique_elements = []
    for element in list_input:
        if not list_input.count(element) > 1:
            list_of_unique_elements.append(element)
    return list_of_unique_elements


lista_a_unique2 = get_unique_elements(lista_a)
# print out
print(MESSAGE_INPUTS.format(list_input=lista_a))
print(MESSAGE_OUTPUTS.format(lista_output=lista_a_unique2))