# Project: cotanct book
# Date: 2018-06-28
# Version: 0.0.4
# Author: Michał Ryś
# Description: Here is contact book database
# Version log:
#   0.0.4 : update after code review 1, finish.
#   0.0.3 : entry as dict
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------
from time import gmtime, strftime

# about this project
CB_VERSION = '0.0.4'
CB_TITLE = '>>>Contact Book MR<<<'

CB_EXIT_WITHOUT_SAVE = ['exit', 'e', 'E', 'Q', 'q', 'quit']

# database files
DB_FILE_01 = 'database4\_test.csv'

# default inputs for entry
time_of_run_program = strftime("%Y-%m-%d--%H-%M-%S", gmtime())
LACK_OF_DATA = '---'

# database default entry
DB_ENTRY = {'date_of_creation': time_of_run_program,
            'name_first': LACK_OF_DATA,
            'name_second': LACK_OF_DATA,
            'name_last': LACK_OF_DATA,
            'phone_mobile': LACK_OF_DATA,
            'phone_private': LACK_OF_DATA,
            'phone_work': LACK_OF_DATA,
            'e-mail_private': LACK_OF_DATA,
            'e-mail_work': LACK_OF_DATA,
            'address_street_name': LACK_OF_DATA,
            'address_street_number': LACK_OF_DATA,
            'address_flat_number': LACK_OF_DATA,
            'address_city_name': LACK_OF_DATA,
            'address_city_code': LACK_OF_DATA,
            'address_country': LACK_OF_DATA,
            'description': LACK_OF_DATA
            }
# ------------------------------------------------------------------------------
# main menu: list of all options to choose
CB_OPTIONS_KEY = []
for option in range(10):
    CB_OPTIONS_KEY.append(option)

# add menu: list of options:
# CB_ADD_MENU_KEY = []
DB_KEYS = []
for key in DB_ENTRY.keys():
    DB_KEYS.append(key)


# ------------------------------------------------------------------------------
# main menu: options to choose - list of messages
CB_OPTIONS = {}
CB_OPTIONS[CB_OPTIONS_KEY[1]] = 'dodaj nowy wpis'
CB_OPTIONS[CB_OPTIONS_KEY[2]] = 'modyfikuj wpisy (usuń, popraw)'
CB_OPTIONS[CB_OPTIONS_KEY[3]] = 'szukaj'
CB_OPTIONS[CB_OPTIONS_KEY[4]] = 'wyświetl całą książkę adresową'
CB_OPTIONS[CB_OPTIONS_KEY[5]] = 'zamknij program i zapisz bazę'

# add menu: options to choose
CB_ADD_MENU_OPTIONS = {}
CB_ADD_MENU_OPTIONS[DB_KEYS[0]] = 'Dodaj aktualny czas utworzenia'
CB_ADD_MENU_OPTIONS[DB_KEYS[1]] = 'Dodaj pierwsze imię'
CB_ADD_MENU_OPTIONS[DB_KEYS[2]] = 'Dodaj drugie imię'
CB_ADD_MENU_OPTIONS[DB_KEYS[3]] = 'Dodaj nazwisko'
CB_ADD_MENU_OPTIONS[DB_KEYS[4]] = 'Dodaj numer komórki'
CB_ADD_MENU_OPTIONS[DB_KEYS[5]] = 'Dodaj numer telefonu prywatnego'
CB_ADD_MENU_OPTIONS[DB_KEYS[6]] = 'Dodaj numer służbowy'
CB_ADD_MENU_OPTIONS[DB_KEYS[7]] = 'Dodaj e-mail prywatny'
CB_ADD_MENU_OPTIONS[DB_KEYS[8]] = 'Dodaj e-mail służbowy'
CB_ADD_MENU_OPTIONS[DB_KEYS[9]] = 'Dodaj nazwę ulicy'
CB_ADD_MENU_OPTIONS[DB_KEYS[10]] = 'Dodaj numer ulicy'
CB_ADD_MENU_OPTIONS[DB_KEYS[11]] = 'Dodaj numer mieszkania'
CB_ADD_MENU_OPTIONS[DB_KEYS[12]] = 'Dodaj nazwę miasta'
CB_ADD_MENU_OPTIONS[DB_KEYS[13]] = 'Dodaj kod miasta'
CB_ADD_MENU_OPTIONS[DB_KEYS[14]] = 'Dodaj nazwę państwa'
CB_ADD_MENU_OPTIONS[DB_KEYS[15]] = 'Dodaj extra opis'

# search menu: options to choose
CB_SEARCH_MENU_OPTIONS = {}
CB_SEARCH_MENU_OPTIONS[DB_KEYS[0]] = 'Dodaj aktualny czas utworzenia'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[1]] = 'Dodaj pierwsze imię'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[2]] = 'Dodaj drugie imię'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[3]] = 'Dodaj nazwisko'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[4]] = 'Dodaj numer komórki'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[5]] = 'Dodaj numer telefonu prywatnego'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[6]] = 'Dodaj numer służbowy'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[7]] = 'Dodaj e-mail prywatny'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[8]] = 'Dodaj e-mail służbowy'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[9]] = 'Dodaj nazwę ulicy'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[10]] = 'Dodaj numer ulicy'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[11]] = 'Dodaj numer mieszkania'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[12]] = 'Dodaj nazwę miasta'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[13]] = 'Dodaj kod miasta'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[14]] = 'Dodaj nazwę państwa'
CB_SEARCH_MENU_OPTIONS[DB_KEYS[15]] = 'Dodaj extra opis'

# ------------------------------------------------------------------------------
# messages
MESSAGE_INTRO = f'Witaj w {CB_TITLE}.'

# messages info
MESSAGE_INFO_CB_VERSION = f'[info]: Wersja programu to {CB_VERSION}'
MESSAGE_INFO_CB_TITLE = f'[info]: Nazwa programu to {CB_TITLE}'

# messages extra
MESSAGE_SEPARATOR = 82 * '-'

# messages ask user for action
MESSAGE_ASK_WHAT_TO_DO = 'Wybierz opcję:'

# main menu: messages options to choose
MESSAGE_CHOICE_WRONG_INPUT = f'[info] Zły wybór, nic nie robie.'
MESSAGE_CHOICE_ADD_NEW = \
    f'[{CB_OPTIONS_KEY[1]}]: {CB_OPTIONS[CB_OPTIONS_KEY[1]]}.'

MESSAGE_CHOICE_MODIFY = \
    f'[{CB_OPTIONS_KEY[2]}]: {CB_OPTIONS[CB_OPTIONS_KEY[2]]}.'

MESSAGE_CHOICE_EXIST = \
    f'[{CB_OPTIONS_KEY[3]}]: {CB_OPTIONS[CB_OPTIONS_KEY[3]]}.'

MESSAGE_CHOICE_DATABASE_PRINT_ALL = \
    f'[{CB_OPTIONS_KEY[4]}]: {CB_OPTIONS[CB_OPTIONS_KEY[4]]}.'

MESSAGE_CHOICE_CB_CLOSE = \
    f'[{CB_OPTIONS_KEY[5]}]: {CB_OPTIONS[CB_OPTIONS_KEY[5]]}.'

# messages for option database print all
MESSAGE_CHOICE_DATABASE_PRINT_ALL_INFO = '[info] Obecna zawartość książki adresowej:'


