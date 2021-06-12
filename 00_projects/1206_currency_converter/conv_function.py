import requests


def get_currencies(url):
    data = requests.get(url).json()
    # подключаюсь по ссылке и достаю из нее данные в json
    currencies = data['rates']  # сохраняю словарь с курсами валют
    return currencies


def convert(from_c, to_c, amount, rate):
    """
    Конвертировать сумму денег из одной валюты в другую
    :param from_c: из какой валюты идет конвертация
    :param to_c: в какую валюту идет конвертация
    :param amount: сумма денег
    :return: итоговое значение
    """
    initial_amount = amount
    if from_c != 'USD':
        amount = amount / rate[from_c]
    # округлю до 4 символов после запятой
    amount = round(amount * rate[to_c], 4)
    return amount
