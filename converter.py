def convert_length(value, from_unit, to_unit):
    units = {
        "мм": 1,
        "см": 10,
        "м": 1000,
        "км": 1000000,
    }
    return value * units[from_unit] / units[to_unit]

def convert_time(value, unit_from, unit_to):
    units = {
        "секунды": 1,
        "минуты": 60,
        "часы": 3600,
        "дни": 86400,
        "месяцы": 2592000,
        "годы": 31536000
    }

    if unit_from not in units or unit_to not in units:
        raise ValueError("Неподдерживаемые единицы измерения времени.")

    seconds = value * units[unit_from]
    result = seconds / units[unit_to]
    return result

def convert_currency(value, currency_from, currency_to):
    exchange_rates = {
        "рубль": {
            "доллар": 0.013,
            "евро": 0.011,
            "рубль": 1
        },
        "доллар": {
            "рубль": 75,
            "евро": 0.85,
            "доллар": 1
        },
        "евро": {
            "рубль": 88,
            "доллар": 1.18,
            "евро": 1
        }
    }

    if currency_from not in exchange_rates or currency_to not in exchange_rates:
        raise ValueError("Неподдерживаемые валюты.")

    if currency_from == currency_to:
        return value

    rate = exchange_rates[currency_from][currency_to]
    result = value * rate
    return result
