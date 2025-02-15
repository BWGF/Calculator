import unittest
import math
from complexFunc import logarithm, factorial, root, sine, cosine, tangent, cotangent, power

class TestComplexFunc(unittest.TestCase):

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(1, 10), 0)
        self.assertEqual(logarithm(math.e, math.e), 1)
        self.assertIn("Неверные аргументы логарифма", logarithm(-1, 10))
        self.assertIn("Неверные аргументы логарифма", logarithm(10, -2))
        self.assertIn("Неверные аргументы логарифма", logarithm(10, 1))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertIn("Факториал можно вычислить только для неотрицательного целого числа", factorial(-1))
        self.assertIn("Факториал можно вычислить только для неотрицательного целого числа", factorial(3.5))

    def test_root(self):
        self.assertEqual(root(16, 2), 4)
        self.assertEqual(root(27, 3), 3)
        self.assertIn("Корень четной степени из отрицательного числа не определен", root(-8, 2))
        self.assertEqual(root(-8, 3), -2)

    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(math.pi / 2), 1)
        self.assertAlmostEqual(sine(math.pi), 0)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(math.pi / 2), 0)
        self.assertAlmostEqual(cosine(math.pi), -1)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(math.pi), 0)
        self.assertAlmostEqual(tangent(math.pi / 4), 1)
        self.assertIn("Тангенс не определен для данного значения", tangent(math.pi / 2))
        self.assertIn("Тангенс не определен для данного значения", tangent(3 * math.pi / 2))

    def test_cotangent(self):
        self.assertAlmostEqual(cotangent(math.pi / 4), 1)
        self.assertAlmostEqual(cotangent(math.pi / 6), root(3, 2))
        self.assertAlmostEqual(cotangent(math.pi / 2), 0)
        self.assertIn("Катангенс не определен для данного значения", cotangent(math.pi))
        self.assertIn("Катангенс не определен для данного значения", cotangent(0))

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertIn("Нельзя возвести отрицательное число в дробную степень", power(-2, 0.5))


if __name__ == "__main__":
    unittest.main()