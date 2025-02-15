def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль")
    return x / y


def percentage(x, y=None):
    if y is None:
        return x / 100
    return (x * y) / 100