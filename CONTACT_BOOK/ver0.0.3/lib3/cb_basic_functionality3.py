# Project: cotanct book
# Date: 2018-06-26
# Version: 0.0.3
# Author: Michał Ryś
# Description: Here are main functions for realise the general ideas of project.
# Version log:
#   0.0.3 : entry as dict
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
# list of own exceptions
class ErrorWrongAge(Exception):
    pass

class ErrorWrongNameIsNotAlpha(Exception):
    pass

class FileDataBaseWithSingleRowError(Exception):
    pass

class ErrorWrongNumberError(Exception):
    pass

class ErrorEmptyDatabaseToWrite(Exception):
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
    import csv
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
    import csv

    # check if database is empty
    # TODO: add check if there is none or single data
    if len(db_whole_as_dict) == 0:
        raise ErrorEmptyDatabaseToWrite
        return []

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
        raise ErrorWrongNameIsNotAlpha

    string_input = string_input.lower()
    string_input = string_input.capitalize()

    return string_input

def get_number_user(message_to_print):
    """Get phone number"""
    # TODO: divide into cell-phone, sign -, +48, (012), ' ', so on...
    string_input = input(f'>>> {message_to_print}: ')

    if not string_input.isdigit:
        raise ErrorWrongNumberError

    number_output = int(string_input)
    # TODO: check if is 123456789, and so on...
    return number_output