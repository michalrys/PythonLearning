# 2018-06-16
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework

# wybierz losowo element z listy
# ------------------------------------------------------------------------------

# functions
def get_element_random_from_list(list_input: list) -> object:
    """Get random element from input list.

    :param list_input: List of elements - any kind is possible.
    :return: Single random element from list.
    """
    from random import randint
    list_input_length = len(list_input)
    index_random = randint(0, list_input_length - 1)
    return list_input[index_random]

def check_01(list_user, how_many_times = 100):
    """For check only. Check 01: function get_element_random_from_list check.

    :param list_user: User list.
    :param how_many_times: How many times check will be done.
    :return: Expectations: random value should be random :D.
    """
    idx = 1
    while idx <= how_many_times:
        list_user_random_element = get_element_random_from_list(list_user)
        print(MESSAGE_OUTPUT.format(element_plot=list_user_random_element))
        idx += 1

# constants
MESSAGE_INPUT = 'Twoja lista to: {list_plot}.'
MESSAGE_OUTPUT = 'Losowy element z listy to: {element_plot}.'

# main
list_user = [2, 4, 23, 6]
list_user_random_element = get_element_random_from_list(list_user)
print(MESSAGE_INPUT.format(list_plot=list_user))
print(MESSAGE_OUTPUT.format(element_plot=list_user_random_element))

# check 01:
check_01(list_user)