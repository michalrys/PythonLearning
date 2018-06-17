# Project: cotanct book
# Version: 0.0.1
# Author: Michał Ryś
# Description: Here is contact book database
# Version log:
#   0.0.1 : preliminary work
# ------------------------------------------------------------------------------

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
CB_DATA_TYPE_11 = '*free_slot_for_future_work*'
CB_DATA_TYPE_12 = '*free_slot_for_future_work*'
CB_DATA_TYPE_13 = '*free_slot_for_future_work*'
CB_DATA_TYPE_14 = '*free_slot_for_future_work*'
CB_DATA_TYPE_15 = '*free_slot_for_future_work*'

# definition of main datebase
cb_database = []

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
