# 2018-07-02
# InfoShare: day 11.
# M. Ryś
# kwiaciarnia - z tablicy
# ------------------------------------------------------------------------------

class Kwiat:
    def __init__(self, cena, rodzaj):
        self.cena = cena
        self.rodzaj = rodzaj

    def __str__(self):
        return self.rodzaj

    def __repr__(self):
        return self.__str__()

class Bukiet:
    def __init__(self, zbior_kwiatow):
        self.zbior_kwiatow = zbior_kwiatow

    def cena(self):
        cena = 0
        for kwiat in self.zbior_kwiatow:
            cena += kwiat.cena
        return cena

class Kwiaciarnia:
    def __init__(self):
        self.kwiaty = []
        self.bukiety = []
    def dodaj_bukiet(self, bukiet):
        self.bukiety.append(bukiet)
    def dodaj_kwiat(self, kwiat, ilosc = 1):
        for i in range(ilosc):
            self.bukiety.append(kwiat)

tulipan = Kwiat(5, 'tulipan')
print(tulipan.cena, tulipan.rodzaj)

b = Bukiet([tulipan, tulipan, tulipan])
print(b.zbior_kwiatow, 'cena to:', b.cena())

kw = Kwiaciarnia()
kw.dodaj_bukiet(b)
kw.dodaj_kwiat(tulipan)

print(kw.bukiety, kw.kwiaty)