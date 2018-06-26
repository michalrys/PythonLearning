# zapis do pliku

# database files
DB_FILE_01 = 'test_writer.csv'

LACK_OF_DATA = '--'
# database default entry
DB_ENTRY = {'date_of_creation': 'sdfasdf',
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

db_whole_as_dict = []

db_whole_as_dict.append(DB_ENTRY)
db_whole_as_dict.append(DB_ENTRY)
db_whole_as_dict.append(DB_ENTRY)

key_list = []

for key in db_whole_as_dict[0]:
    key_list.append(key)

print(key_list)

def db_data_write(db_whole_as_dict, db_file):
    """Write whole database to file"""
    import csv

    key_list = []
    for key in db_whole_as_dict[0]:
        key_list.append(key)

    with open(db_file, mode='w', encoding='utf-8', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=key_list)
        writer.writeheader()
        for entry in db_whole_as_dict:
            writer.writerow(entry)

db_data_write(db_whole_as_dict, DB_FILE_01)



