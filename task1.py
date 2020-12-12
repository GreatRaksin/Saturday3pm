'''
Создать словарь со странами и их столицами

Вывести предложение:

{столица} is a capital of {страна}.
'''

countries = {
  'USA': 'Minsk',
  'Brazil': 'Brasilia',
  'Belarus': 'Washington',
  'Italy': 'Rome',
  'Spain': 'Madrid'
}

for country, capital in countries.items():
  print(f'{capital} is a Capital of {country}')


fr = {
  9: 'nine',
  10: True
}