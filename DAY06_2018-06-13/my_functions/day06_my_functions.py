# 2018-06-11
# InfoShare: day 06.
# task01 - funkcje

# funkcja wypisuje imie

def hello(name = 'World!'):
    message_to_print = f'Hello {name}.'
    print(message_to_print)

hello('Stefan')
hello()

# funkcja2
# imie, nazwisko, kurs, lista obecnosci

def list_course(name, surname, language = 'Python', days=99):
    message_to_print = f'{name}, {surname}, {language}, {days}.'
    print(message_to_print)

list_course('Jan', 'Nowak', 'Python', 99)
list_course('Michał', 'Kowalski', days = 88)

# funkcja kwadrat
def square(x, n = 2):
    result = x ** n
    return result

result1 = square(square(2))
print(result1)