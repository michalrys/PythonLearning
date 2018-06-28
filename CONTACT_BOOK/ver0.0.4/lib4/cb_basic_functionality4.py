# Project: cotanct book
# Date: 2018-06-28
# Version: 0.0.4
# Author: Michał Ryś
# Description: Here are main functions for realise the general ideas of project.
# Version log:
#   0.0.4 : update after code review 1, finish.
#   0.0.3 : entry as dict
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
import csv
from time import gmtime, strftime

# list of own exceptions
class WrongAgeError(Exception):
    pass

class WrongNameIsNotAlphaError(Exception):
    pass

class FileDataBaseWithSingleRowError(Exception):
    pass

class WrongNumberError(Exception):
    pass

class EmptyDatabaseToWriteError(Exception):
    pass

# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# work with files
def db_data_read(db_file):
    """Read database file and return db whole as list of dicts"""
    db_whole_as_list = []
    db_whole_as_dict = []

    try:
        with open(db_file, mode='r', encoding='utf-8',
                  newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            how_many_entries = 0
            for row in spamreader:
                db_whole_as_list.append(row)
                how_many_entries += 1
        if how_many_entries == 1:
            raise FileDataBaseWithSingleRowError
    except FileNotFoundError:
        print('[error]: Plik nie istnieje. Nie wczytano danych.')
        print(f'[info]: Po wyjściu z programu, zostanie utworzony '
              f'plik z bazą danych: {db_file}')
        return []
    except FileDataBaseWithSingleRowError:
        print('[error]: Plik istnieje, ale ma tylko jedną linijkę. '
              'Zatem, zgodnie ze schematem zapisu, są to tylko etykiety. '
              'Dlatego nie wczytano danych.')
        print(f'[info]: Po wyjsciu z progrmu, zostanie utworzony '
              f'plik z bazą danych: {db_file}')
        return []

    else:
        # TODO: make backup file
        # create database as:  [ {}_1, {}_2, ... ]
        db_list_of_keys = db_whole_as_list[0]

        for entry in db_whole_as_list[1:]:
            temp_keys_zipped_with_values = zip(db_list_of_keys, entry)
            temp_single_entry_as_dict = dict(temp_keys_zipped_with_values)
            db_whole_as_dict.append(temp_single_entry_as_dict)
        print(f'[info]: Pomyślnie wczytano bazę danych: {db_file}')

        return db_whole_as_dict

def db_data_write(db_whole_as_dict, db_file):
    """Write whole database as list of dicts to csv file"""

    # check if database is empty
    # TODO: add check if there is none or single data
    if len(db_whole_as_dict) == 0:
        raise EmptyDatabaseToWriteError

    key_list = []
    for key in db_whole_as_dict[0]:
        key_list.append(key)

    with open(db_file, mode='w', encoding='utf-8', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=key_list)
        writer.writeheader()
        for entry in db_whole_as_dict:
            writer.writerow(entry)


# ------------------------------------------------------------------------------
# get different kind of input data
def get_name_user(message_to_print):
    """Get name"""
    string_input = input(f'>>> {message_to_print}: ')

    if not string_input.isalpha():
        raise WrongNameIsNotAlphaError

    string_input = string_input.lower()
    string_input = string_input.capitalize()

    return string_input

def get_number_user(message_to_print):
    """Get phone number"""
    # TODO: divide into cell-phone, sign -, +48, (012), ' ', so on...
    string_input = input(f'>>> {message_to_print}: ')

    if not string_input.isdigit:
        raise WrongNumberError

    number_output = int(string_input)
    # TODO: check if is 123456789, and so on...
    return number_output

# menu add ---------------------------------------------------------------------
def cb_add_menu_print_what_to_do(message_separator, message_ask_what_to_do, db_keys, menu_options):
    """Prints what to do in menu add"""
    # input
    # MESSAGE_SEPARATOR, MESSAGE_ASK_WHAT_TO_DO, DB_KEYS, CB_ADD_MENU_OPTIONS,

    print(message_separator)
    # print options to choose
    print(message_ask_what_to_do)

    for db_key in db_keys:
        temp_len = len(menu_options[db_key])
        temp_len_must_be = 35
        temp_len_arrow = temp_len_must_be - temp_len
        print(f'{menu_options[db_key]}', sep='', end='')
        print(' ', temp_len_arrow * '-', '> ', sep='', end='')
        print(f'{db_key}', sep='', end='\n')
    print('Aby wypełnić wszystko po kolei: add')
    print('Aby cofnąć się do menu głównego wpisz: back')
    print('Aby zapisać i wrócić do menu głównego wpisz: done')

def cb_add_menu_execute_choosen_option(db_new_entry, add_menu_option):
    """Execute option in add menu"""
    # input: add_menu_option, db_new_entry
    # output: db_new_entry

    if add_menu_option == 'date_of_creation':
        print('Dodano aktualną datę jako datę utworzenia wpisu.')
        time_current = strftime("%Y-%m-%d--%H-%M-%S", gmtime())
        db_new_entry['date_of_creation'] = time_current

    elif add_menu_option == 'name_first':
        try:
            name_input = get_name_user('Pierwsze imię to')
        except WrongNameIsNotAlphaError:
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

        # ...
    elif add_menu_option == 'back':
        print('Cofa się do menu głównego i nic nie robi')

    elif add_menu_option == 'done':
        print('Do bazy dodano następujący wpis:')
        print(db_new_entry)


    else:
        print(f'Wybrana opcja: {add_menu_option} jest nieprawidłowa.')

    return (db_new_entry, add_menu_option)



# menu search ------------------------------------------------------------------
def cb_search_menu_print_what_to_do(message_separator, message_ask_what_to_do, db_keys, menu_options):
    """Prints what to do in menu add"""
    # input
    # MESSAGE_SEPARATOR,MESSAGE_ASK_WHAT_TO_DO, DB_KEYS, CB_SEARCH_MENU_OPTIONS

    print(message_separator)
    # print options to choose
    print(message_ask_what_to_do)
    # TODO: change this loop for function

    for search_menu_key in db_keys:
        temp_len = len(menu_options[search_menu_key])
        temp_len_must_be = 35
        temp_len_arrow = temp_len_must_be - temp_len
        print(f'{menu_options[search_menu_key]}', sep='', end='')
        print(' ', temp_len_arrow * '-', '> ', sep='', end='')
        print(f'{search_menu_key}', sep='', end='\n')
    print('Aby cofnąć się do menu głównego wpisz: back')

def cb_search_menu_execute_choosen_option(search_menu_option):
    """Execute option in search menu"""
    # input: search_menu_option
    # output: search_data_value, search_data_type

    if search_menu_option == 'date_of_creation':
        time_current = strftime("%Y-%m-%d--%H-%M-%S", gmtime())
        print(f'Podaj datę, np: {time_current}')
        search_data_value = cb_get_string_from_user('Data')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')


    elif search_menu_option == 'name_first':
        print('Podaj pierwsze imię, np: Michał')
        search_data_value = cb_get_string_from_user('Imię pierwsze')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')

    elif search_menu_option == 'name_second':
        print('Podaj drugie imię, np: Stanisław')
        search_data_value = cb_get_string_from_user('Imię drugie')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')

    elif search_menu_option == 'name_last':
        print('Podaj nazwisko, np: Nowak')
        search_data_value = cb_get_string_from_user('Nazwisko')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')

    elif search_menu_option == 'phone_mobile':
        # TODO: do data check
        print('Podaj numer komórki, np: 01234567')
        search_data_value = get_number_user('Telefon komórkowy')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')

    elif search_menu_option == 'phone_private':
        # TODO: do data check
        print('Podaj numer telefonu prywatnego, np: 01234567')
        search_data_value = get_number_user('Telefon prywatny')
        search_data_type = search_menu_option
        return (search_data_value, search_data_type, 'back')

        # ...

    elif search_menu_option == 'back':
        print('Cofa się do menu głównego i nic nie robi')
        search_data_value = search_menu_option
        search_data_type = None
        return (search_data_value, search_data_type, 'back')
    else:
        print(f'Wybrana opcja: {search_menu_option} jest nieprawidłowa.')
        search_data_value = search_menu_option
        search_data_type = None
        return (search_data_value, search_data_type, search_menu_option)


def get_entries_from_db(db_whole_as_dict, data_type, data_value):
    """Get entries from db which contain data_value. Return list of dicts"""

    if data_type == None:
        return []
    db_whole_as_dict_entry_locations = []

    for idx, entry in enumerate(db_whole_as_dict):
        if entry[data_type] == data_value:
            db_whole_as_dict_entry_locations.append(idx)

    return db_whole_as_dict_entry_locations


def print_entities_by_location_from_db(db_whole_as_dict,
                                       db_whole_as_dict_entry_locations,
                                       search_data_type,
                                       search_data_value,
                                       message_separator):
    """Print entities by location from database """

    if bool(db_whole_as_dict_entry_locations):
        print(message_separator)
        print(message_separator)
        print('Znaleziono:')
        for entry_id in db_whole_as_dict_entry_locations:
            print(f'[{entry_id}] --> ', sep='', end='')
            print(db_whole_as_dict[entry_id])
        print(message_separator)
    else:
        print(message_separator)
        print(message_separator)
        print(f'! nie znaleziono {search_data_type} = {search_data_value} !')
        print(message_separator)