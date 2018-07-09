class Kwiat:
    def __init__(self, cena, rodzaj):
        if cena < 0:
            raise ValueError
        self.cena = cena
        self.rodzaj = rodzaj

    def __str__(self):
        return self.rodzaj

    def __repr__(self):
        return self.__str__()


class Bukiet:
    def __init__(self, zbior_kwiatow):
        self.zbior_kwiatow = zbior_kwiatow

    @property
    def cena(self):
        cena = 0
        for kwiat in self.zbior_kwiatow:
            cena += kwiat.cena
        return cena


class Kwiaciarnia:
    kwiaty = []
    bukiety = []

    @classmethod
    def dodaj_bukiet(cls, bukiet):
        cls.bukiety.append(bukiet)

    @classmethod
    def dodaj_kwiat(cls, kwiat, ilosc=1):
        for i in range(ilosc):
            cls.kwiaty.append(kwiat)

#
# kwiat_test = Kwiat(-20, 'testowy')
#
# tulipan = Kwiat(5, 'tulipan')
# print(tulipan.rodzaj)
# print(tulipan.cena)
#
# b = Bukiet([tulipan, tulipan])
# print(b.zbior_kwiatow)
# print("Cena: ", b.cena)
#
# kw = Kwiaciarnia()
# kw.dodaj_bukiet(b)
# kw.dodaj_kwiat(tulipan, ilosc=10)
#
# print(kw.bukiety)
# print(kw.kwiaty)
#
# # inne kwiaciarnie
# kw2 = Kwiaciarnia()
# kw2.dodaj_bukiet(b)
# kw2.dodaj_kwiat(tulipan, ilosc=50)
#
# print(kw2.bukiety)
# print(kw2.kwiaty)
