# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework 01

# napisz program sumujący wszystkie elementy w liscie
# ------------------------------------------------------------------------------

# constants, varibales
MESSAGE_SUM_1 = 'Suma elementów w liście = {sum_of_el}'

# create list
list_user = [4, 3, 6, 10, 8, 50]

# TODO: check type of elements --> int? float?
# TODO: create function: create user list

# sum up elements in list
list_sum_of_all_elements = 0

# method #1 for loop
for element in list_user:
    list_sum_of_all_elements += element

print(f'[Metoda 1 = pętla for]: ', sep='', end='')
print(MESSAGE_SUM_1.format(sum_of_el = list_sum_of_all_elements))


# ------------------------------------------------------------------------------
# method #2 while loop
list_sum_of_all_elements = 0
list_length = len(list_user)
element_id = 0

while element_id < list_length:
    list_sum_of_all_elements += list_user[element_id]
    element_id += 1

print(f'[Metoda 2 = pętla while]: ', sep='', end='')
print(MESSAGE_SUM_1.format(sum_of_el = list_sum_of_all_elements))

# ------------------------------------------------------------------------------
# TODO: method #3 built-in functions/methods
# TODO: poszukać, na razie nie znalazłem !!

# ------------------------------------------------------------------------------
# method #4 function
def sum_of_elements_from_list (list_input: list, type_of_elements: str = 'int') :
    """Sum all elements from input list. Elements must have the same type -
    default is integer.

    :param list list_input: list of numbers
    :param str type_of_elements: type of numbers
    :return : sum of numbers, the same type as elements in list
    """
    sum_of_elements = 0
    if type_of_elements == 'int':
        for element in list_input:
            if type(element) == int:
                sum_of_elements += element
            else:
                print(f'[error]: Wrong input list. There should be integers only.')
                print(f'[error]: this: {element} is not int type.')
                print(f'[error]: Function aborted.')
                return 0
    elif type_of_elements == 'float':
        for element in list_input:
            if type(element) == float:
                sum_of_elements += element
            else:
                print(f'[error]: Wrong input list. There should be integers only.')
                print(f'[error]: this: {element} is not int type.')
                print(f'[error]: Function aborted.')
                return 0
    else:
        #TODO: in future
        pass
    return sum_of_elements

# for tests only:
list_user = [2.0 , 4.2]
# list_user = [2 , 4.1]
# list_user = [2.0 , 'asdf']

list_sum_of_all_elements = sum_of_elements_from_list(list_user, 'float')
print(f'[Metoda 4 = pętla while]: ', sep='', end='')
print(MESSAGE_SUM_1.format(sum_of_el = list_sum_of_all_elements))