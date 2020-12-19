from openpyxl import Workbook

workbook = Workbook()  # создаем Excel-табличку
sheet = workbook.active  # открывает лист у таблицы

sheet['A1'] = 'hello'
sheet['B1'] = 'world!'

workbook.save(filename='hello_world.xlsx')

