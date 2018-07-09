from unittest import TestCase

from kwiaciarnia import Kwiat
from kwiaciarnia import Bukiet
from kwiaciarnia import Kwiaciarnia


class TestKwiaciarnia(TestCase):

    def test_check_if_object_is_instance_of_kwiat(self):
        k = Kwiat(12, 'rose')
        self.assertIsInstance(k, Kwiat)

    def test_check_if_constructur_sets_price_and_name(self):
        k = Kwiat(43, 'tulip')
        self.assertEqual(43, k.cena)
        self.assertEqual('tulip', k.rodzaj)

    def test_check_object___str__(self):
        k = Kwiat(43, 'tulip')
        self.assertEqual('tulip', str(k))

    def test_price_of_flower(self):
        k = Kwiat(100.5, 'tulip')
        self.assertEqual(100.5, k.cena)

    def test_price_price_is_not_number(self):
        k = Kwiat('sto zlotych', 'tulip')
        self.assertRaises(ValueError)

    def test_kwiat_in_bukiet(self):
        k = Kwiat(55, 'tulip')
        b = Bukiet([k, k])
        self.assertIn(k, b.zbior_kwiatow)

    def test_price_price_has_value_below_zero(self):
        with self.assertRaises(ValueError):
            k = Kwiat(int(-20), 'tulip')

