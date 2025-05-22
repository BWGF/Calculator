import math


def logarithm(x):
    try:
        if x <= 0:
            raise ValueError("Логарифм определен только для положительных чисел")
        return math.log10(x)
    except ValueError as e:
        return str(e)


def factorial(x):
    try:
        if not isinstance(x, int) or x < 0:
            raise ValueError("Факториал можно вычислить только для неотрицательного целого числа")
        return math.factorial(x)
    except ValueError as e:
        return str(e)

def root(x):
    try:
        if x < 0:
            raise ValueError("Квадратный корень из отрицательного числа не определен")
        return x ** (1 / 2)
    except ValueError as e:
        return str(e)


def sine(x):
    try:
        return math.sin(x)
    except Exception as e:
        return str(e)


def cosine(x):
    try:
        return math.cos(x)
    except Exception as e:
        return str(e)


def is_tangent_undefined(x, tolerance=1e-10):
    n = round((x - math.pi / 2) / math.pi)
    critical_point = math.pi / 2 + n * math.pi
    return abs(x - critical_point) < tolerance


def tangent(x):
    try:
        if is_tangent_undefined(x):
            raise ValueError("Тангенс не определен для данного значения")
        result = math.tan(x)
        if abs(result) > 1e15:
            raise ValueError("Тангенс не определен для данного значения")

        return result

    except ValueError as e:
        return str(e)


def cotangent(x):
    try:
        tan = tangent(x)
        if isinstance(tan, str):
            if "Тангенс не определен для данного значения" in tan:
                return 0
            raise ValueError(tan)
        if abs(tan) > 1e15:
            return 0
        if abs(tan) < 1e-15:
            raise ValueError("Катангенс не определен для данного значения")

        return 1 / tan

    except ValueError as e:
        return str(e)


def power(x, y):
    try:
        if x < 0 and not y.is_integer():
            raise ValueError("Нельзя возвести отрицательное число в дробную степень")
        return x ** y
    except ValueError as e:
        return str(e)
