import unittest
from person import Person
# osobna klasa do testow


class TestPerson(unittest.TestCase):
    def test_check_constructor_sets_name_and_surname(self):
        p = Person("Jan", "Kowalski")

        self.assertEqual(p.name, "Jan")
        self.assertEqual(p.surname, "Kowalski")

    def test_check_if_person_has_full_name(self):
        p = Person("Jan", "Kowalski")

        self.assertTrue(hasattr(p, 'full_name'))

    def test_checks_if_full_name_is_actually_full_name(self):
        p = Person("Jan", "Kowalski")

        self.assertEqual(
            'Kowalski, Jan',
            p.full_name
        )

# if __name__ == '__main__':
#     unittest.main()
