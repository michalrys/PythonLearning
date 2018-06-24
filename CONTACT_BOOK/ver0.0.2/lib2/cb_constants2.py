# Project: cotanct book
# Date: 2018-06-24
# Version: 0.0.2
# Author: Michał Ryś
# Description: Here is contact book database
# Version log:
#   0.0.2 : working on file, exceptions
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------

# about this project
CB_VERSION = '0.0.2'
CB_TITLE = '>>>Contact Book MR<<<'

# database files
DB_FILE_01 = 'database\cb_database01.csv'

# database keys
DB_KEYS = []
for option in range(11):
    DB_KEYS.append(option)

# database dictionary values
DB_ENTRIES = {}
DB_ENTRIES[DB_KEYS[0]] = 'date_of_creation'
DB_ENTRIES[DB_KEYS[1]] = 'first_name'
DB_ENTRIES[DB_KEYS[2]] = 'second_name'
DB_ENTRIES[DB_KEYS[3]] = 'surname'
DB_ENTRIES[DB_KEYS[4]] = 'phone_number'
DB_ENTRIES[DB_KEYS[5]] = 'address_street_name'
DB_ENTRIES[DB_KEYS[6]] = 'address_street_number'
DB_ENTRIES[DB_KEYS[7]] = 'address_flat_number'
DB_ENTRIES[DB_KEYS[8]] = 'address_city_name'
DB_ENTRIES[DB_KEYS[9]] = 'address_city_code'
DB_ENTRIES[DB_KEYS[10]] = 'address_country'
# DB_ENTRIES[DB_KEYS[11]] = '*free_slot_for_future_work*'
# DB_ENTRIES[DB_KEYS[12] = '*free_slot_for_future_work*'
# DB_ENTRIES[DB_KEYS[13] = '*free_slot_for_future_work*'
# DB_ENTRIES[DB_KEYS[14] = '*free_slot_for_future_work*'
# DB_ENTRIES[DB_KEYS[15] = '*free_slot_for_future_work*'
# ------------------------------------------------------------------------------
# # create empty file
# separator = ','
# cb_database_csv_string = separator.join(DB_ENTRIES.values())
# print(cb_database_csv_string)
#
# with open('..\database\cb_database01356.csv', 'a', encoding='utf-8', newline='\n') as file:
#     file.write(cb_database_csv_string)
#     file.write('\n')
# ------------------------------------------------------------------------------

# list of all options to choose
CB_OPTIONS_KEY = []
for option in range(10):
    CB_OPTIONS_KEY.append(option)

# options to choose - list of messages
CB_OPTIONS = {}
CB_OPTIONS[CB_OPTIONS_KEY[1]] = 'dodaj imię'
CB_OPTIONS[CB_OPTIONS_KEY[2]] = 'usuń imię'
CB_OPTIONS[CB_OPTIONS_KEY[3]] = 'sprawdź czy imię jest w bazie'
CB_OPTIONS[CB_OPTIONS_KEY[4]] = 'wyświetl całą książkę adresową'
CB_OPTIONS[CB_OPTIONS_KEY[5]] = 'zamknij program'

# messages
MESSAGE_INTRO = f'Witaj w {CB_TITLE}.'

# messages info
MESSAGE_INFO_CB_VERSION = f'[info]: Wersja programu to {CB_VERSION}'
MESSAGE_INFO_CB_TITLE = f'[info]: Nazwa programu to {CB_TITLE}'

# messages extra
MESSAGE_SEPARATOR = 82 * '-'

# messages ask user for action
MESSAGE_ASK_WHAT_TO_DO = 'Wybierz opcję:'

# messages options to choose
MESSAGE_CHOICE_WRONG_INPUT = f'[info] Zły wybór, nic nie robie.'
MESSAGE_CHOICE_NAME_ADD = \
    f'[{CB_OPTIONS_KEY[1]}]: {CB_OPTIONS[CB_OPTIONS_KEY[1]]}.'

MESSAGE_CHOICE_NAME_REMOVE = \
    f'[{CB_OPTIONS_KEY[2]}]: {CB_OPTIONS[CB_OPTIONS_KEY[2]]}.'

MESSAGE_CHOICE_NAME_EXIST = \
    f'[{CB_OPTIONS_KEY[3]}]: {CB_OPTIONS[CB_OPTIONS_KEY[3]]}.'

MESSAGE_CHOICE_DATABASE_PRINT_ALL = \
    f'[{CB_OPTIONS_KEY[4]}]: {CB_OPTIONS[CB_OPTIONS_KEY[4]]}.'

MESSAGE_CHOICE_CB_CLOSE = \
    f'[{CB_OPTIONS_KEY[5]}]: {CB_OPTIONS[CB_OPTIONS_KEY[5]]}.'

# messages for option database print all
MESSAGE_CHOICE_DATABASE_PRINT_ALL_INFO = '[info] Obecna zawartość książki adresowej:'


