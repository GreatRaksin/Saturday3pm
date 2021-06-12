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

intro_label = Label(root, text='Welcome to RT Currency Converter',
                    fg='blue', font=('Arial', 18, 'bold'),
                    relief=RAISED)
intro_label.place(x=100, y=5)
date_label = Label(root, text=f'1 USD = {convert("USD", "BYN", 1, cur)} BYN',
                   font=('Arial', 22, 'bold'), fg='green')
date_label.place(x=160, y=40)


# поля для ввода
amount_field = Entry(root, justify=CENTER)  # сюда вводят сумму
converted_amount = Entry(root, text='', justify=CENTER)  # сюда будем вписывать конвертированный итог

# выпадающие списки
from_currency_var = StringVar()
from_currency_var.set('USD')  # валюта по умолчанию
to_currency_var = StringVar()
to_currency_var.set('BYN')  # валюта по умолчанию

font = ('Arial', 12, 'bold')
root.option_add('*TCombobox*Listbox.font', font)  # добавляю значения для выпадающих списков
from_dropdown = ttk.Combobox(textvariable=from_currency_var,  # это текст, который отображается по умолчанию
                             values=list(cur.keys()),  # записываю все валюты
                             font=font,
                             justify=CENTER)
to_dropdown = ttk.Combobox(textvariable=to_currency_var,  # это текст, который отображается по умолчанию
                             values=list(cur.keys()),  # записываю все валюты
                             font=font,
                             justify=CENTER)

# расположение
from_dropdown.place(x=30, y=90)
amount_field.place(x=30, y=110)

to_dropdown.place(x=250, y=90)
converted_amount.place(x=250, y=110)


def perform():
    amount = float(amount_field.get())
    f_cur = from_currency_var.get()
    to_cur = to_currency_var.get()

    converted = convert(f_cur, to_cur, amount, cur)

    converted_amount.delete(0, END)
    converted_amount.insert(0, str(converted))
# кнопка "конвертировать"
btn = Button(root, text='Convert!',
             fg='red', font=('Arial', 10, 'bold'),
             command=perform)
btn.place(x=200, y=150)


if __name__ == '__main__':
    root.mainloop()