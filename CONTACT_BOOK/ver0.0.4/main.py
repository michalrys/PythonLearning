# Project: cotanct book
# Date: 2018-06-28
# Version: 0.0.4
# Author: Michał Ryś
# Description: This is main function to run.
# Version log:
#   0.0.4 : update after code review 1, finish.
#   0.0.3 : database: list of dicts.
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
import copy
from lib4.cb_constants4 import *
from lib4.cb_basic_functionality4 import *

# main loop
run_program = True
print(MESSAGE_INTRO)

# read database from file
db_whole_as_dict = db_data_read(DB_FILE_01)

while run_program:
    print(MESSAGE_SEPARATOR)

    print(MESSAGE_ASK_WHAT_TO_DO,
          MESSAGE_CHOICE_ADD_NEW,
          MESSAGE_CHOICE_MODIFY,
          MESSAGE_CHOICE_EXIST,
          MESSAGE_CHOICE_DATABASE_PRINT_ALL,
          MESSAGE_CHOICE_CB_CLOSE,
          sep='\n')

    option_choosen = cb_get_char_from_user()

    # OPTION EXIT --------------------------------------------------------------
    if option_choosen in CB_EXIT_WITHOUT_SAVE:
        print('! wyjście bez zapisu !')
        break

    # OPTION WRONG not decimal -------------------------------------------------
    elif not option_choosen.isdecimal():
        print(MESSAGE_CHOICE_WRONG_INPUT)

    # OPTION 1 --------- ADD NEW DATA MODULE -----------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[1]:
        # IMPORTANT !!! to use deepcopy
        db_new_entry = copy.deepcopy(DB_ENTRY)

        add_menu_option = ''

        while not add_menu_option == 'back':
            cb_add_menu_print_what_to_do(MESSAGE_SEPARATOR,
                                         MESSAGE_ASK_WHAT_TO_DO,
                                         DB_KEYS,
                                         CB_ADD_MENU_OPTIONS)
            # read input string from user
            add_menu_option = cb_get_char_from_user()

            # execute option
            add_menu_result_of_chosen_option = \
                cb_add_menu_execute_choosen_option(db_new_entry,
                                                   add_menu_option)

            db_new_entry.update(add_menu_result_of_chosen_option[0])
            add_menu_option = add_menu_result_of_chosen_option[1]

            # check if add new entry to database
            # TODO: function?
            if add_menu_option == 'done':
                # TODO: add exception: if no new data, dont add entry to db
                print('Do bazy dodano następujący wpis:')
                print(db_new_entry)
                db_whole_as_dict.append(db_new_entry)
                add_menu_option = 'back'

    # OPTION 2 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[2]:
        # modify entry
        pass
        # 1. wybierz wpis -> przez id / imie / nazwisko
        # 2. wyświetl te wpisy
        # 3. wybierz któryś z nich do edycji
        # 4. zrób to co w add menu - tylko bez deepcopy

        #
        #

    # OPTION 3 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[3]:
        # check if data (eg. name) is in database
        search_data_value = ''
        search_menu_option = ''
        search_data_type = None

        while not search_menu_option == 'back':
            # TODO: merge add_menu & search_menu functions?
            cb_search_menu_print_what_to_do(MESSAGE_SEPARATOR,
                                            MESSAGE_ASK_WHAT_TO_DO,
                                            DB_KEYS,
                                            CB_SEARCH_MENU_OPTIONS)
            # read input string from user
            search_menu_option = cb_get_char_from_user()

            # execute chosen option
            search_menu_result_of_chosen_option = \
                cb_search_menu_execute_choosen_option(search_menu_option)

            search_data_value = search_menu_result_of_chosen_option[0]
            search_data_type = search_menu_result_of_chosen_option[1]
            search_menu_option = search_menu_result_of_chosen_option[2]

        # check search_data_value in database
        db_whole_as_dict_entry_locations = get_entries_from_db(
            db_whole_as_dict, search_data_type, search_data_value)

        # print what was found:
        print_entities_by_location_from_db(db_whole_as_dict,
                                           db_whole_as_dict_entry_locations,
                                           search_data_type,
                                           search_data_value,
                                           MESSAGE_SEPARATOR)

    # OPTION 4 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[4]:
        # print out whole contact book
        # TODO: improve later
        for entry in db_whole_as_dict:
            print(entry)

    # OPTION 5 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[5]:
        # exit
        run_program = False

        # write all entries to database: db_whole_as_dict --> file.csv
        try:
            db_data_write(db_whole_as_dict, DB_FILE_01)
        except EmptyDatabaseToWriteError:
            print('Baza danych jest pusta. Nic nie zapisuję. '
                  'Wychodzę z programu.')

    # OPTION ELSE --------------------------------------------------------------
    else:
        print(MESSAGE_CHOICE_WRONG_INPUT)
