# Project: cotanct book
# Date: 2018-06-26
# Version: 0.0.3
# Author: Michał Ryś
# Description: This is main function to run.
# Version log:
#   0.0.3 : database: list of dicts.
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
import copy
from time import gmtime, strftime
from lib3.cb_constants3 import *
from lib3.cb_basic_functionality3 import *

from cb_constants3 import *
from cb_basic_functionality3 import *

# TODO: check working ctrl+q

# main loop
exit_program = 'No'
print(MESSAGE_INTRO)

# read database from file
db_whole_as_dict = db_data_read(DB_FILE_01)

while exit_program == 'No':
    print(MESSAGE_SEPARATOR)

    print(MESSAGE_ASK_WHAT_TO_DO,
          MESSAGE_CHOICE_ADD_NEW,
          MESSAGE_CHOICE_MODIFY,
          MESSAGE_CHOICE_EXIST,
          MESSAGE_CHOICE_DATABASE_PRINT_ALL,
          MESSAGE_CHOICE_CB_CLOSE,
          sep='\n')

    option_choosen = cb_get_char_from_user()
    #print(option_choosen)

    # check what option was choosen

    # OPTION 1 --------- ADD NEW DATA MODULE -----------------------------------
    if int(option_choosen) == CB_OPTIONS_KEY[1]:
        # new empty entry is created - filled with '---' -> look at constants
        # IMPORTANT !!!
        db_new_entry = copy.deepcopy(DB_ENTRY)

        add_menu_option = ''

        while not add_menu_option == 'back':
            print(MESSAGE_SEPARATOR)

            # print options to choose
            print(MESSAGE_ASK_WHAT_TO_DO)
            # TODO: change this loop for function
            for add_menu_key in CB_ADD_MENU_OPTIONS.keys():
                temp_len = len(CB_ADD_MENU_OPTIONS[add_menu_key])
                temp_len_must_be = 35
                temp_len_arrow = temp_len_must_be - temp_len
                print(f'{CB_ADD_MENU_OPTIONS[add_menu_key]}', sep='', end='')
                print(' ', temp_len_arrow * '-', '> ', sep='', end='')
                print(f'{add_menu_key}', sep='', end='\n')
            print('Aby wypełnić wszystko po kolei: add')
            print('Aby cofnąć się do menu głównego wpisz: back')
            print('Aby zapisać i wrócić do menu głównego wpisz: done')

            # read input string from user
            add_menu_option = cb_get_char_from_user()

            # ------------------------------------------------------------------
            # execute choosen option -------------------------------------------
            if add_menu_option == 'date_of_creation':
                print('Dodano aktualną datę jako datę utworzenia wpisu.')
                time_current = strftime("%Y-%m-%d--%H-%M-%S", gmtime())
                db_new_entry['date_of_creation'] = time_current

            elif add_menu_option == 'name_first':
                try:
                    name_input = get_name_user('Pierwsze imię to')
                except ErrorWrongNameIsNotAlpha:
                    print(f'Podane imię ma niedozwolone znaki.')
                else:
                    db_new_entry['name_first'] = name_input
                    print('[info]: OK, dodano.')

            elif add_menu_option == 'name_second':
                name_input = get_name_user('Drugie imię to')
                db_new_entry['name_second'] = name_input
                print('[info]: OK, dodano.')

            elif add_menu_option == 'name_last':
                name_input = get_name_user('Nazwisko to')
                db_new_entry['name_last'] = name_input
                print('[info]: OK, dodano.')

            elif add_menu_option == 'phone_mobile':
                number_input = get_number_user('Numer komórki to')
                db_new_entry['phone_mobile'] = number_input
                print('[info]: OK, dodano.')

            elif add_menu_option == 'phone_private':
                number_input = get_number_user('Numer prywatny telefonu to')
                db_new_entry['phone_mobile'] = number_input
                print('[info]: OK, dodano.')

            elif add_menu_option == 'add':
                print('Dodaje wszystko pokolei. Do zrobienia potem.')

                #...
            elif add_menu_option == 'back':
                print('Cofa się do menu głównego i nic nie robi')
            elif add_menu_option == 'done':
                print('Do bazy dodano następujący wpis:')
                print(db_new_entry)
                db_whole_as_dict.append(db_new_entry)

                add_menu_option = 'back'
            else:
                print(f'Wybrana opcja: {add_menu_option} jest nieprawidłowa.')


    # OPTION 2 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[2]:
        pass
        #
        #
        #

    # OPTION 3 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[3]:
        # check if name is in database

        # get input data
        first_name_to_check_input = cb_get_string_from_user('Pierwsze imię to')

        print('Do zrobienia')

    # OPTION 4 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[4]:
        # print out all contact book
        # TODO: improve
        for entry in db_whole_as_dict:
            print(entry)

    # OPTION 5 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[5]:
        # exit
        exit_program = 'Yes'

        # write all entries to database: db_whole_as_dict --> file.csv
        db_data_write(db_whole_as_dict, DB_FILE_01)

    # OPTION not decimal -------------------------------------------------------
    elif not option_choosen.isdecimal():
        print(MESSAGE_CHOICE_WRONG_INPUT)

    # OPTION ELSE --------------------------------------------------------------
    else:
        print(MESSAGE_CHOICE_WRONG_INPUT)