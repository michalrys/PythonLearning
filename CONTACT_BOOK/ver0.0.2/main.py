# Project: cotanct book
# Date: 2018-06-24
# Version: 0.0
# Author: Michał Ryś
# Description: This is main function to run.
# Version log:
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
from lib2.cb_constants2 import *
from lib2.cb_basic_functionality2 import *

from cb_constants2 import *
from cb_basic_functionality2 import *

# TODO: check working ctrl+q

# main loop
exit_program = 'No'
print(MESSAGE_INTRO)

while exit_program == 'No':
    print(MESSAGE_SEPARATOR)

    print(MESSAGE_ASK_WHAT_TO_DO,
          MESSAGE_CHOICE_NAME_ADD,
          MESSAGE_CHOICE_NAME_REMOVE,
          MESSAGE_CHOICE_NAME_EXIST,
          MESSAGE_CHOICE_DATABASE_PRINT_ALL,
          MESSAGE_CHOICE_CB_CLOSE,
          sep='\n')

    option_choosen = cb_get_char_from_user()
    #print(option_choosen)

    # check what option was choosen

    # OPTION 1 -----------------------------------------------------------------
    if int(option_choosen) == CB_OPTIONS_KEY[1]:
        # add name to contact book
        try:
            first_name_input = get_name_user('Podaj pierwsze imie')
        except ErrorWrongNameIsNotAlpha:
            print('[error]: Zła wartość. Imie musi zawierać tylko litery.')
            print('[info]: Przerywam. Wychodzę do menu głownego')
        else:
            db_new_entry = db_data_empty(DB_KEYS, 'no-data')
            db_new_entry = db_data_update(1, db_new_entry, first_name_input)
            db_data_append(db_new_entry, DB_FILE_01)

    # OPTION 2 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[2]:
        # remove names from contact book
        # TODO: wczytanie danych jako słownik ?
        # TODO: dane = 'imie,nazwisko,data'
        # TODO: slownik_z_danych_01 = dict(  zip( range(3),dane.split(',') )  )
        # potem :  plik = [dane1, dane2, ... , danen]
        # potem zmiana:  id w liscie -> zmiana w słowniku
        # potem zapis: przeiterować listę -> zapis słowników albo join
        #
        # //albo pozbycie się list i tylko w petli szukanie po słownikach ?//
        #
        #
        #

        first_name_to_check_input = cb_get_string_from_user('Usuń pierwsze imię')

        print('Do zrobienia')

    # OPTION 3 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[3]:
        # check if name is in database

        # get input data
        first_name_to_check_input = cb_get_string_from_user('Pierwsze imię to')

        print('Do zrobienia')

    # OPTION 4 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[4]:
        # print out all contact book
        print(MESSAGE_CHOICE_DATABASE_PRINT_ALL_INFO)
        print('Do zrobienia')

    # OPTION 5 -----------------------------------------------------------------
    elif int(option_choosen) == CB_OPTIONS_KEY[5]:
        # exit
        exit_program = 'Yes'

    # OPTION not decimal -------------------------------------------------------
    elif not option_choosen.isdecimal():
        print(MESSAGE_CHOICE_WRONG_INPUT)

    # OPTION ELSE --------------------------------------------------------------
    else:
        print(MESSAGE_CHOICE_WRONG_INPUT)