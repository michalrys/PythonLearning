# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework 02

# znajdz najwiekszy / najmniejszy element w lisci
# ------------------------------------------------------------------------------

# constants, variables, messages
MESSAGE_LIST_REVIEW = 'Twoja lista to: {list_to_print}.'
MESSAGE_LIST_EXTR_REVIEW = '{extremum_type} liczba z listy to element o id: ' \
                           '{element_id} o wartości: {element_value}.'

# input user list
list_user = [3, 4, 6, 9, 44, 9, -3, 49]

# TODO: function to create user list
# TODO: validate if elements are int, float, numbers

# method #1 for loop
list_user_element_max = list_user[0]
list_user_element_max_id = 0

list_user_element_min = list_user[0]
list_user_element_min_id = 0

for idx, element in enumerate(list_user):
    # look for max
    if element > list_user_element_max:
        list_user_element_max = element
        list_user_element_max_id = idx
    else:
        pass
    # look for min
    if element < list_user_element_min:
        list_user_element_min = element
        list_user_element_min_id = idx
    else:
        pass

# print out results
print(MESSAGE_LIST_REVIEW.format(list_to_print=list_user))
print(MESSAGE_LIST_EXTR_REVIEW.format(extremum_type='Największa',
                                      element_id=list_user_element_max_id,
                                      element_value=list_user_element_max))

print(MESSAGE_LIST_EXTR_REVIEW.format(extremum_type='Najmniejsza',
                                      element_id=list_user_element_min_id,
                                      element_value=list_user_element_min))

# TODO: rebuild for functions: create_list, find_extremum,
