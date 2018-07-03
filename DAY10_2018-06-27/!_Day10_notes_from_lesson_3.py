# 2018-06-27
# InfoShare: day 10.
# M. Ryś
# OBIEKTY
# ------------------------------------------------------------------------------
class Person(object):
    def __init__(self):
        pass

print(Person)
print(Person())
print(82 * '-')

janek = Person()

# tak też można definiować
janek.name = 'Janek'
janek.surname = 'Nowak'

# to jest wada, bo jak zrobimy
ola = Person()
ola.pseudonim = 'Krokodyl'

# mamy w efekcie klasę Person, która ma różne metody !
# ------------------------------------------------------------------------------

class Person2(object):
    def __init__(self, imie, nazwisko, pseudonim='nick_name'):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pseudonim = pseudonim

    def __str__(self):
        return self.przedstaw_sie()

    def __add__(self, other):
        return Person2("Jas Junior", self.nazwisko+"-"+other.nazwisko)

    def przedstaw_sie(self):
        return (f'Jestem: {self.imie} {self.nazwisko}. A mój nick to: {self.pseudonim}')

jasiu = Person2('Jasiu', 'Kowalski', 'Stefan')
# jasiu.przedstaw_sie()
ola = Person2('Ola', 'Nowak', 'Krokodyl')
print(str(jasiu))
print(str(ola))

print(jasiu + ola)
