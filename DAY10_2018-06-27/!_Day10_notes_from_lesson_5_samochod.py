# 2018-06-27, day 10, M. Ryś
# ------------------------------------------------------------------------------
class PojazdMechaniczny(object):
    def __init__(self, silnik):
        self.silnik = silnik

    def odpal_silnik(self):
        print('Silnik uruchomiono.')

class Samochod(PojazdMechaniczny):
    def __init__(self, marka, model, pojemnosc_silnika):
        super().__init__(pojemnosc_silnika)  #<<<< wchodzi do metody klasy bazowej i dadaje - nie przysłania
        self.marka = marka
        self.model = model

    def zatrab(self, krotnosc=1):
        beep_sound = 'beep '
        print('>> ', krotnosc * beep_sound, '<<', sep='')

    def status(self):
        print(f'Marka: {self.marka}, '
              f'model: {self.model}, '
              f'silnik ma pojemność: {self.silnik}.')

# ------------------------------------------------------------------------------
my_car1 = Samochod('Fiat', 'Punto', pojemnosc_silnika='1.2')
my_car1.status()
print(82 * '-')
my_car1.zatrab(5)

print(my_car1.silnik)
my_car1.odpal_silnik()

print(my_car1.silnik)
print(len(my_car1.silnik))