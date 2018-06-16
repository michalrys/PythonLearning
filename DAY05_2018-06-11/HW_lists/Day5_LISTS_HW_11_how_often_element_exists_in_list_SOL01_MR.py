# 2018-06-16
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework

# oblicz częstość elementów w liście (ile razy)
# jedna wersja zwykla pętle, ify itd
# druga - moze jest jakis modul gotowy???
# ------------------------------------------------------------------------------

# functions
def get_amount_of_element_in_list(element_to_find: object, list_input: object) -> int:
    #TODO: make more complex
    """Count occurrance of element in list.

    :rtype: int
    :param object element_to_find: Element to find.
    :param list list_input: List of elements.
    :return: Amount of element in list.
    """
    amount_of_element_in_list = 0
    for element in list_input:
        if element == element_to_find:
            amount_of_element_in_list += 1
    return amount_of_element_in_list

def get_percentage_of_element_occurance_in_list(amount_of_element: int,
                                                list_length: int) -> int:
    """Calculate % of element from element list.

    :rtype: int
    :param int amount_of_element: How many times specified element exist in list.
    :param int list_length: Total amount of element which exist in list.
    :return:
    """
    element_occurance_in_perc = (amount_of_element / list_length) * 100
    return element_occurance_in_perc

def get_unique_list(list_user: list) -> list:
    """Delete duplicates from list.

    :rtype: list
    :param list list_user: List to work in.
    :return: List with uniques elements.
    """
    list_user_unique = list(set(list_user))
    return list_user_unique

# constants
MESSAGE_INPUT = 'Statystka elementów dla listy:\n{list_plot}'
MESSAGE_OUTPUT = 'Element: {element}, ' \
                 'wystąpił {element_count} razy, co ' \
                 'stanowi {element_stats:.0f}% elementów listy.'

# input list
list_user = [10,10,20,10,10,20,10,20,20,20,40,50,40,10,30,50,50,30]

# main
list_user_length = len(list_user)
list_user_unique = get_unique_list(list_user)
element_statistic = []
element_how_many = []

for element in list_user_unique:
    element_count = get_amount_of_element_in_list(element, list_user)
    element_statistic.append(
        get_percentage_of_element_occurance_in_list(element_count,
                                                    list_user_length))
    element_how_many.append(element_count)

print(MESSAGE_INPUT.format(list_plot=list_user))
for idx, element_unique in enumerate(list_user_unique):
    print(MESSAGE_OUTPUT.format(element=element_unique,
                                element_count=element_how_many[idx],
                                element_stats=element_statistic[idx]))
