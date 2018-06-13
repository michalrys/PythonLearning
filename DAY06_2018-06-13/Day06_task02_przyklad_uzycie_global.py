# 2018-06-11
# InfoShare: day 06.
# task02 - funkcje

# funkcja wypisuje imie

name_global = 'Jan'

def name_change(new_name):
    global name_global
    name_global = new_name

def name_print(name_to_print):
    print(name_to_print)

print('Przed zmianą: ')
name_print(name_global)

print('Po zmianie:')
name_change('Janek')
name_print(name_global)


