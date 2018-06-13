# 2018-06-13
# InfoShare: day 06. Notatki z zajęć. 2
# M. Ryś

# funkcje -> potem import
# return, docstringi

# tworzymy reużywalny kod
# funkcja = blok kodu, który chcemy reużywać

def foo(working_list = []):
    working_list.append("a")
    print(working_list)

foo()
foo()

