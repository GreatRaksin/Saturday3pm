# Task 1. Почтовое отправление

def post(name):
    print(f'''
    {name},
    Belarus, Minsk, Minsk dist.,
    20080, Kiseleva 12, apt. 20''')


post('Demid Raksin')
post('Jagor Tereshonok')


def tax_rate(price, rate):
    #res = price + ((price * rate) / 100)
    percents = (price * rate) / 100
    result = price + percents
    return result, percents


price, rate = tax_rate(1000, 8)
print(f'Цена (итог): {price}')
print(f'Переплата: {rate}')
'''
Если одно из возвращаемых функцией значений не нужно,
называем переменную для сохранения этого значения
знаком _
'''