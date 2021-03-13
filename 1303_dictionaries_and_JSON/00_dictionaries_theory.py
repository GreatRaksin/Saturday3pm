'''Словарь - это набор пар ключ:значение.
Самое главное отличие словаря от списка -
это наличие в нем ключей.
'''

pallette = {
    'red': '#ff335c',
    'yellow': '#ffff85',
    'mint': '#3eb489',
    'violet': '#9933ff'
}  # для того, чтобы достать значение из словаря,
# нужно обратиться к имени словаря, а в [] указать
# название !!!КЛЮЧА!!!
print(f"My favourite color is {pallette['violet']}!")
# это не работает: print(f"My favourite color is {pallette['#ff335c']}!")
print(pallette.keys())  # чтобы увидеть список всех ключей