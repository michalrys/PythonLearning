# Project: cotanct book
# Date: 2018-06-24
# Version: 0.0
# Author: Michał Ryś
# Description: Here are main functions for realise the general ideas of project.
# Version log:
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
# list of own exceptions
class ErrorWrongAge(Exception):
    pass

class ErrorWrongNameIsNotAlpha(Exception):
    pass


# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
def get_name_user(message_to_print):
    """Get name"""
    string_input = input(f'>>> {message_to_print}: ')

    if not string_input.isalpha():
        raise ErrorWrongNameIsNotAlpha

    string_input = string_input.lower()
    string_input = string_input.capitalize()

    return string_input

def db_data_empty(db_keys, db_value_empty_tag):
    """Create empty entry"""
    db_entry_empty = {}

    for key in db_keys:
        db_entry_empty[key] = f'{db_value_empty_tag}'
    return db_entry_empty


def db_data_update(db_key, db_entry, new_value):
    """Update value in entry via key number."""
    # DB_ENTRIES[DB_KEYS[0]] = 'date_of_creation'
    # DB_ENTRIES[DB_KEYS[1]] = 'first_name'
    # DB_ENTRIES[DB_KEYS[2]] = 'second_name'
    # DB_ENTRIES[DB_KEYS[3]] = 'surname'
    # DB_ENTRIES[DB_KEYS[4]] = 'phone_number'
    # DB_ENTRIES[DB_KEYS[5]] = 'address_street_name'
    # DB_ENTRIES[DB_KEYS[6]] = 'address_street_number'
    # DB_ENTRIES[DB_KEYS[7]] = 'address_flat_number'
    # DB_ENTRIES[DB_KEYS[8]] = 'address_city_name'
    # DB_ENTRIES[DB_KEYS[9]] = 'address_city_code'
    # DB_ENTRIES[DB_KEYS[10]] = 'address_country'
    db_entry[db_key] = new_value
    return db_entry

def db_data_append(db_entry, db_file):
    """Write new line of data to database."""
    data_separator = ','
    cb_data_to_write_in_csv_format = data_separator.join(db_entry.values())

    with open(db_file, mode='a', encoding='utf-8', newline='\n') as file:
        file.write(cb_data_to_write_in_csv_format)
        file.write('\n')