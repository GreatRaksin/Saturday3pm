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
}  # для того, чтобы достать значение из словаря,
# в котором есть вложенные элементы, необходимо
# обращаться в строгой очередности по элементам
print(pallette['red'][2]['original_red'])
