# 2018-06-26
# mrys
# wczytanie bazy danych do słownika
import csv

PLIK_SCIEZKA = 'dane_test.csv'
db_whole_as_list = []
db_whole_as_dict = []

try:
    with open(PLIK_SCIEZKA, mode='r', encoding='utf-8', newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            db_whole_as_list.append(row)
except FileNotFoundError:
    print('Plik nie istnieje. Nie wczytano danych.')
    print(f'Po wyjsciu z progrmu, zostanie utworzony plik z bazą danych: {PLIK_SCIEZKA}')
else:
    # create database as:  [ {}_1, {}_2, ... ]
    db_list_of_keys = db_whole_as_list[0]
    for entry in db_whole_as_list[1:]:
        temp_keys_zipped_with_values = zip(db_list_of_keys, entry)
        temp_single_entry_as_dict = dict(temp_keys_zipped_with_values)
        db_whole_as_dict.append(temp_single_entry_as_dict)

    print(db_whole_as_dict[0])