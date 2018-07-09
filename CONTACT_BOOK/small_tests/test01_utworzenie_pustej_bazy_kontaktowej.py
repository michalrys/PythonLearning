# for test only

# constants
CB_DATA_TYPE_0 = 'id_data'
CB_DATA_TYPE_1 = 'first_name'
CB_DATA_TYPE_2 = 'second_name'
CB_DATA_TYPE_3 = 'surname'
CB_DATA_TYPE_4 = 'phone_number'
CB_DATA_TYPE_5 = 'address_street_name'
CB_DATA_TYPE_6 = 'address_street_number'
CB_DATA_TYPE_7 = 'address_flat_number'
CB_DATA_TYPE_8 = 'address_city_name'
CB_DATA_TYPE_9 = 'address_city_code'
CB_DATA_TYPE_10 = 'address_country'


# row 0 is for description of database
cb_database = [[CB_DATA_TYPE_0,
                CB_DATA_TYPE_1,
                CB_DATA_TYPE_2,
                CB_DATA_TYPE_3,
                CB_DATA_TYPE_4,
                CB_DATA_TYPE_5,
                CB_DATA_TYPE_6,
                CB_DATA_TYPE_7,
                CB_DATA_TYPE_8,
                CB_DATA_TYPE_9,
                CB_DATA_TYPE_10,
               ]]

# print(cb_database[0][:])

separator = ','

cb_database_csv_string = separator.join(cb_database[0][:])

print(cb_database_csv_string)

with open('..\database\cb_database01.csv', 'w', encoding='utf-8') as file:
    file.write(cb_database_csv_string)

