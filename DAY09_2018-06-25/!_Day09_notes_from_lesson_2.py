# 2018-06-25
# InfoShare: day 09.
# M. Ryś
#
# OBIEKTY
# ------------------------------------------------------------------------------
class Samochod(object):
    def __init__(self, marka, model, light = 'Turned off'):
        self.marka = marka
        self.model = model
        self.light = light
    def beep_sound(self):
        print(f'My {self.marka} says beeep.')
    def turn_light(self, turn_on):
        if turn_on:
            self.light = 'Turned on'
        else:
            self.light = 'Turned off'
    def print_status(self):
        print(f'Marka: {self.marka}, model: {self.model}, światła: {self.light}')


my_car1 = Samochod('Fiat', 'Punto')

print(f'Twoje auto to: {my_car1.marka} {my_car1.model}.')
print(f'Stan świateł to: {my_car1.light}')
print(82 * '-')
my_car1.beep_sound()
my_car1.turn_light('True')
my_car1.print_status()