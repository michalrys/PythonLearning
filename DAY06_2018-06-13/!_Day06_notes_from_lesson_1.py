# 2018-06-13
# InfoShare: day 06. Notatki z zajęć.
# M. Ryś

# funkcje -> potem import
# return, docstringi

# tworzymy reużywalny kod
# funkcja = blok kodu, który chcemy reużywać

def do_nothing():
    pass

def do_nothing():
    # sd
    return None

# wywołąnie funkcji: funkcja(argumenty - jeśli są)

# funkcje argumentowe
# named arguments, keyword arguements = to są argumenty z domyślnymi wartościami

def rectan_field(x, y=10):
    field = x * y
    print(f'Pole: {x} * {y} = {field}')
    return field

rectan_field(2)


# w pythonie wszystko jest obiektem. Funkcje też. Dlatego, można zrobić coś takiego
# x przypisujemy funkcje print. teraz x działa jak print.
x = print
x('Pawel')

