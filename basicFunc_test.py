import unittest
from basicFunc import add, subtract, multiply, divide, percentage

class TestBasicFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_percentage(self):
        self.assertEqual(percentage(100, 50), 50)
        self.assertEqual(percentage(100), 1)
        self.assertEqual(percentage(0, 50), 0)
        self.assertEqual(percentage(100, 0), 0)

if __name__ == "__main__":
    unittest.main()