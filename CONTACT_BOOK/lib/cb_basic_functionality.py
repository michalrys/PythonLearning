# Project: cotanct book
# Version: 0.0.1
# Author: Michał Ryś
# Description: Here are main functions for realise the general ideas of project.
# Version log:
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------

def cb_print_messages(*args: object) -> None:
    """Print any kind and any number of object - dedicated for messages.

    :rtype: None
    :param object args: Any kind of object, any number. It is recommended to
                        use strings.
    :return: Print out on strandart output.
    """
    for message in args:
        print(message)

def cb_print_list_2d(matrix: list) -> object:
    """Print elements of 2d list.

    :rtype: None
    :param list matrix: List must be 2d --> [[...],[...],[...],...]
    :return: Print out at strandard output.
    """
    #TODO make more complex
    for row in matrix:
        print('|', sep=' ', end='')
        for element in row:
            print( ' ', element, ' ', sep='', end='')
        print('|', sep=' ', end='\n')

def cb_get_char_from_user() -> str:
    """Get single char from user via standard input.

    :rtype: str
    :return: Single char.
    """
    #TODO: must be single char, else repeat
    #TODO: must be alphanumeric char, else repeat
    char_input_from_user = input('>>> ')
    return char_input_from_user

def cb_get_string_from_user(message_to_print: str) -> object:
    """Get string from user via standard input.

    :rtype: str
    :param str message_to_print: Message to display.
    :return: String from user.
    """
    #TODO: must be string, else repeat
    #TODO: add check for names, surenames, nicks, address, ...
    string_input_from_user = input(f'>>> {message_to_print}: ')
    return string_input_from_user

def cb_add_empty_row_to_database(database_main_list: list) -> None:
    """Database: add new empty row.

    :rtype: None
    :param database_main_list: Database to modify.
    :return: New empty row in list.
    """
    value_for_new_data = '-no-data-'
    # TODO: !! check it
    cb_database = database_main_list
    # TODO: add here exception - later
    # cb_database_last_data_id = int(cb_database[-1][0])

    # append new row as a copy of row 0
    cb_database.append(cb_database[0][:])

    # put
    for idx, _ in enumerate(cb_database[-1][:]):
        cb_database[-1][idx] = value_for_new_data

    # increase data id
    cb_database_last_data_id = 0
    for row in cb_database[0:-1]:
        cb_database_last_data_id += 1
    cb_database[-1][0] = cb_database_last_data_id

def cb_add_to_database(database_main_list: list, data_type: int, data_value: str,
                       id_data: int = 'add_as_new_data'):
    """Database: add item to database (2d list).

    :rtype: none
    :param list database_main_list: Database as a 2d list.
    :param int data_type: For definition go to cd_database.py.
    :param str data_value: String data.
    :param int id_data: Location in database. Look at cd_database.py.
    :return: New row in database = 2d list, with user input name.
    """
    # TODO: !! check it
    cb_database = database_main_list
    # TODO: ?? maybe use global?
    CB_DATA_TYPE_0 = 0
    CB_DATA_TYPE_1 = 1
    CB_DATA_TYPE_2 = 2
    CB_DATA_TYPE_3 = 3
    CB_DATA_TYPE_4 = 4
    CB_DATA_TYPE_5 = 5
    CB_DATA_TYPE_6 = 6
    CB_DATA_TYPE_7 = 7
    CB_DATA_TYPE_8 = 8
    CB_DATA_TYPE_9 = 9
    CB_DATA_TYPE_10 = 10

    # add data as a new data
    if id_data == 'add_as_new_data':
        cb_add_empty_row_to_database(cb_database)
        id_data = int(-1)
    else:
        # when user give id data -> number
        # TODO: check input data -> numeric, other
        id_data = int(id_data)

    # check what to add
    if data_type == CB_DATA_TYPE_1:
        # insert first name
        cb_database[id_data][1] = data_value
    elif data_type == CB_DATA_TYPE_2:
        # insert second name
        cb_database[id_data][2] = data_value
    else:
        # TODO: add all types of data
        # TODO: add here exception
        pass

def cb_get_how_many_item_by_name_in_database(database_main_list: list,
                                             data_type: int,
                                             data_value: str):
    """Amount of item by its name in database.

    :rtype: none
    :param list database_main_list: Database as a 2d list.
    :param int data_type: For definition go to cd_database.py.
    :param str data_value: String data.
    :return:
    """
    # TODO: opis -> sprawdza i zwraca ile razy wystapilo
    # TODO: !! check it
    cb_database = database_main_list
    # TODO: !! check it, improve
    CB_DATA_TYPE_0 = 0
    CB_DATA_TYPE_1 = 1
    CB_DATA_TYPE_2 = 2
    CB_DATA_TYPE_3 = 3
    CB_DATA_TYPE_4 = 4
    CB_DATA_TYPE_5 = 5
    CB_DATA_TYPE_6 = 6
    CB_DATA_TYPE_7 = 7
    CB_DATA_TYPE_8 = 8
    CB_DATA_TYPE_9 = 9
    CB_DATA_TYPE_10 = 10

    # check if name exists in database
    # TODO: check if list is 1d !
    data_type_count_in_database = 0

    if int(data_type) == CB_DATA_TYPE_1:
        # check for first name
        for index_of_row, row_of_data in enumerate(cb_database):
            if data_value == cb_database[index_of_row][1]:
                # print('[info] Imie: ', data_value, 'jest w danych id = ', index_of_row)
                data_type_count_in_database += 1

    return data_type_count_in_database

def cb_get_location_item_by_name_in_database(database_main_list: list,
                                             data_type: int,
                                             data_value: str) -> list:
    """Get information where is some item in database by its name.
    Duplicates are also considered.

    :rtype: list
    :param list database_main_list: Database as a 2d list.
    :param int data_type: For definition go to cd_database.py.
    :param str data_value: String data.
    :return: Identification numbers of rows, in which data is located.
    """
    # TODO: opis -> sprawdza i zwraca w ktorym rzędzie jest dana
    # TODO: !! check it
    cb_database = database_main_list
    # TODO: !! check it, improve
    CB_DATA_TYPE_0 = 0
    CB_DATA_TYPE_1 = 1
    CB_DATA_TYPE_2 = 2
    CB_DATA_TYPE_3 = 3
    CB_DATA_TYPE_4 = 4
    CB_DATA_TYPE_5 = 5
    CB_DATA_TYPE_6 = 6
    CB_DATA_TYPE_7 = 7
    CB_DATA_TYPE_8 = 8
    CB_DATA_TYPE_9 = 9
    CB_DATA_TYPE_10 = 10

    # check if name exists in database
    # TODO: check if list is 1d !
    data_location_in_database = []

    if int(data_type) == CB_DATA_TYPE_1:
        # check for first name
        for index_of_row, row_of_data in enumerate(cb_database):
            if data_value == cb_database[index_of_row][1]:
                # print('[info] Imie: ', data_value, 'jest w danych id = ', index_of_row)
                data_location_in_database.append(index_of_row)

    return data_location_in_database


def cb_remove_item_by_name_from_database(database_main_list: list,
                                         data_type: int,
                                         data_value: str,
                                         data_location: list):
    """Delete x1 of defined item be value.

    :rtype: none
    :param list database_main_list: Database as a 2d list.
    :param int data_type: For definition go to cd_database.py.
    :param str data_value: String data.
    :param list data_location: Identification numbers of rows, in which data is
                                located.
    :return:
    """
    # TODO: !! check it
    cb_database = database_main_list
    # TODO: ?? maybe use global?
    CB_DATA_TYPE_0 = 0
    CB_DATA_TYPE_1 = 1
    CB_DATA_TYPE_2 = 2
    CB_DATA_TYPE_3 = 3
    CB_DATA_TYPE_4 = 4
    CB_DATA_TYPE_5 = 5
    CB_DATA_TYPE_6 = 6
    CB_DATA_TYPE_7 = 7
    CB_DATA_TYPE_8 = 8
    CB_DATA_TYPE_9 = 9
    CB_DATA_TYPE_10 = 10

    if int(data_type) == CB_DATA_TYPE_1:
        # remove for first name
        if len(data_location) == 0:
            print(f'[info] Brak w bazie takiego imienia: "{data_value}"')
        elif len(data_location) == 1:
            print(f'[info] W bazie jest dokladnie jedno takie imie: "{data_value}"')
            print(f'[info] Usuwam ten wpis z bazy.')

            cb_database.pop(data_location[0])

        elif len(data_location) > 1:
            print(f'[info] W bazie jest więcej niż jedno imię: "{data_value}"')
            print(f'[info] Wybierz, które mam usunąć: ')

            for index_of_data_to_review in data_location:
                print(f'[info] Wybierz: {index_of_data_to_review}, '
                      f'aby usunąć:', sep='', end='')
                print(cb_database[index_of_data_to_review])

            data_to_delete = input('>>> ')
            data_to_delete = int(data_to_delete)
            data_to_delete_is_correct = False

            for index_of_data in data_location:
                if int(index_of_data) == data_to_delete:
                    cb_database.pop(index_of_data)
                    print(f'[info] Wybrałeś: {data_to_delete}. Usuwam.')
                    data_to_delete_is_correct = True

            if not data_to_delete_is_correct:
                print(f'[info] Wybrałeś: {data_to_delete}. Nie ma takiej '
                          f'opcji. Nic nie robię.')
