# 2018-07-02
# InfoShare: day 11.
# M. Ryś
# figury geometryczne
# ------------------------------------------------------------------------------

class Flower:
    def __init__(self, kind, price):
        self.kind = kind
        self.price = float(price)

    def status(self):
        print(f'Kwiat ma typ: {self.kind}, cenę jednostkową {self.price} PLN.')


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def status(self):
        print(f'Bukiet posiada kwiaty: ')
        for flower in self.flowers:
            print('\t', flower.kind)
        print(f'Cena bukietu to: {self.price()} PLN.')

    def price(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        return price

class FlowerMarket:
    def __init__(self):
        self.flowers = {}
        self.bouquets = {}
        self.flowers_keys = []
        self.bouquets_keys = []

    def update(self, item_object, amount):
        if item_object == 'flower':
            self.flowers[item_object.kind] = amount

# ------------------------------------------------------------------------------

roza_dluga = Flower('rose_long', '5.00')
roza_krotka = Flower('rose_short', '3.00')
tulipan = Flower('tulip', '1.50')

kwiaciarnia_1 = FlowerMarket()
kwiaciarnia_1.update('flower', )

roza_dluga.status()

bukiet_1 = Bouquet()
bukiet_1.add_flower(roza_dluga)
bukiet_1.add_flower(roza_dluga)
bukiet_1.add_flower(roza_krotka)
bukiet_1.add_flower(tulipan)
bukiet_1.add_flower(tulipan)

bukiet_1.status()


