from tkinter import *
from tkinter import ttk

from conv_function import get_currencies, convert
# импортирую функции, которые написал во втором файлике

url = 'https://api.exchangerate-api.com/v4/latest/USD'
cur = get_currencies(url)
print(convert('EUR', 'BYN', 1000, cur))

root = Tk()
root.title('Currency Converter')
root.geometry('500x200')


if __name__ == '__main__':
    root.mainloop()