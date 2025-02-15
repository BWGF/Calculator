import unittest
from converter import convert_time, convert_currency


class TestConverter(unittest.TestCase):

    def test_convert_time(self):
        units = ["секунды", "минуты", "часы", "дни", "месяцы", "годы"]

        self.assertEqual(convert_time(60, "секунды", "минуты"), 1)
        self.assertEqual(convert_time(3600, "секунды", "часы"), 1)
        self.assertEqual(convert_time(86400, "секунды", "дни"), 1)
        self.assertEqual(convert_time(2592000, "секунды", "месяцы"), 1)
        self.assertEqual(convert_time(31536000, "секунды", "годы"), 1)

        for unit in units:
            self.assertEqual(convert_time(1, unit, unit), 1)

        with self.assertRaises(ValueError):
            convert_time(60, "недели", "минуты")
        with self.assertRaises(ValueError):
            convert_time(60, "секунды", "веки")

    def test_convert_currency(self):
        currencies = ["рубль", "доллар", "евро"]

        self.assertAlmostEqual(convert_currency(100, "рубль", "доллар"), 1.3)
        self.assertAlmostEqual(convert_currency(1, "доллар", "рубль"), 75)
        self.assertAlmostEqual(convert_currency(1, "евро", "рубль"), 88)

        for currency in currencies:
            self.assertEqual(convert_currency(1, currency, currency), 1)

        with self.assertRaises(ValueError):
            convert_currency(100, "юань", "доллар")
        with self.assertRaises(ValueError):
            convert_currency(100, "рубль", "фунт")


if __name__ == "__main__":
    unittest.main()