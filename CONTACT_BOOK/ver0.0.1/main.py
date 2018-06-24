# Project: cotanct book
# Version: 0.0.1
# Author: Michał Ryś
# Description: This is main function to run.
# Version log:
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
from lib.cb_constants import *
from lib.cb_database import *
from lib.cb_basic_functionality import *

from cb_basic_functionality import *

# # TODO: gdy dodam tą linię poniżej, wtedy mam podpowiedzi pod ctrl+q
# from cb_basic_functionality import *


# import sys
# print(sys.path)

# main loop


exit_program = 'No'
print(MESSAGE_INTRO)

while exit_program == 'No':
    print(MESSAGE_SEPARATOR)

    cb_print_messages(MESSAGE_ASK_WHAT_TO_DO,
                      MESSAGE_CHOICE_NAME_ADD,
                      MESSAGE_CHOICE_NAME_REMOVE,
                      MESSAGE_CHOICE_NAME_EXIST,
                      MESSAGE_CHOICE_DATABASE_PRINT_ALL,
                      MESSAGE_CHOICE_CB_CLOSE)

    option_choosen = cb_get_char_from_user()
    #print(option_choosen)

    # check what option was choosen

    # OPTION ELSE --------------------------------------------------------------
    # wrong option - not decimal char
    if not option_choosen.isdecimal():
        print(MESSAGE_CHOICE_WRONG_INPUT)

    # OPTION 1 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTION_1:
        first_name_input = cb_get_string_from_user('Pierwsze imię to')
        cb_add_to_database(cb_database, 1, first_name_input, id_data='add_as_new_data')

    # OPTION 2 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTION_2:
        # remove names from contact book
        # TODO: renumber id of data

        first_name_to_check_input = cb_get_string_from_user('Usuń pierwsze imię')

        first_name_to_check_input_amount = \
            cb_get_how_many_item_by_name_in_database(cb_database, 1,
                                                     first_name_to_check_input)

        first_name_to_check_input_locations = \
            cb_get_location_item_by_name_in_database(cb_database, 1,
                                                     first_name_to_check_input)

        cb_remove_item_by_name_from_database(cb_database, 1,
                                             first_name_to_check_input,
                                             first_name_to_check_input_locations)

    # OPTION 3 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTION_3:
        # check if name is in database

        # get input data
        first_name_to_check_input = cb_get_string_from_user('Pierwsze imię to')

        # check how many times input is in database
        first_name_to_check_input_amount = \
            cb_get_how_many_item_by_name_in_database(cb_database, 1,
                                                     first_name_to_check_input)

        # print out
        if first_name_to_check_input_amount > 0:

            first_name_to_check_input_locations = \
                cb_get_location_item_by_name_in_database(cb_database, 1,
                                                         first_name_to_check_input)

            print(f'[info] Podane pierwsze imię: {first_name_to_check_input} '
                  f'występuje {first_name_to_check_input_amount} razy w bazie.')
            print(f'\n[info] Są to wpisy numer: '
                  f'{first_name_to_check_input_locations}')

        else:
            print(f'[info] Podane pierwsze imię: {first_name_to_check_input}, '
                  f'nie występuje w bazie.')

    # OPTION 4 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTION_4:
        # print out all contact book
        print(MESSAGE_CHOICE_DATABASE_PRINT_ALL_INFO)
        cb_print_list_2d(cb_database)

    # OPTION 5 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTION_5:
        # exit
        exit_program = 'Yes'

    # OPTION ELSE --------------------------------------------------------------
    else:
        print(MESSAGE_CHOICE_WRONG_INPUT)
