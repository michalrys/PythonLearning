# 2018-06-14
# Autor: Michał Ryś
# InfoShare: day 05: listy. Homework

# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
# ------------------------------------------------------------------------------

# function definitions
def create_and_get_list():
    #TODO: make more complex
    input_string = str(input('Define list: '))
    new_list = eval(input_string)
    return new_list

def two_lists_have_at_least_one_common_element(list_1st, list_2nd):
    #TODO: make more complex
    for element in list_1st:
        if not list_2nd.count(element) == int(0):
            return True
        else:
            pass
    return False

# constants, messages
MESSAGE_RESULT = 'Dla podanych list: \n' \
                 '{first_list}\n' \
                 '{second_list}\n' \
                 'wynikiem sprawdzenia, czy jest co najmniej 1 wspólny ' \
                 'element w listach jest: {comparison_result}'
MESSAGE_SEPARATOR = 82 * '-'

# main function
list_no1 = create_and_get_list()
list_no2 = create_and_get_list()

lists_have_at_least_1_common_element = \
    two_lists_have_at_least_one_common_element(list_no1, list_no2)

print(MESSAGE_RESULT.format(first_list=list_no1, second_list=list_no2,
                    comparison_result=lists_have_at_least_1_common_element))