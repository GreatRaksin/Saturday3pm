'''Словари можно совмещать с циклами'''

pallette = {
    'red': [
        'peach',
        'orange',
        {
            'coral': '#ff4d4d',
            'original_red': '#ff0000',
            'salmon': '#ff9999'
        }
        ],
    'yellow': '#ffff85',
    'mint': '#3eb489',
    'violet': '#9933ff'
}

# метод .items() достает ВСЮ информацию из словаря
# метод .keys() достанет все КЛЮЧИ из словаря
# метод .values() достанет все ЗНАЧЕНИЯ из словаря
for key, value in pallette.items():
    print(f'Key: {key}')
    print(f'Value: {value}')
    print()

colors = ['red', 'yellow', 'mint', 'violet']
for value in colors:
    print(f'Value in list: {value}')