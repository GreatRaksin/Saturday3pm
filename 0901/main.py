from tkinter import *

root = Tk()  # создаем главное окно
root.geometry('300x200')  # задать размер окна - 300 * 200 пикселей
root.title('Симулятор мастера Йоды')  # текст в названии окошка

# создаем виджеты
e = Entry(width=30)  # поле для ввода чего-либо
b = Button(text='Поехали!')  # кнопка
l = Label(
    bg='#83cef2',
    width=30,
    height=5,
    font='Arial 24 bold italic'
)  # поле для отображения текста


def YodaSay(event):  # создаем функцию, реагирующую на событие
    string = e.get()  # получаю что-то из Entry
    string = string.split()  # разбиваю слова в список
    string.sort()  # сортирую список в алфавитном порядке
    l['text'] = ' '.join(string)


b.bind('<Button-1>', YodaSay)

# функция .pack() "упаковывает" виджеты на экране
e.pack()
b.pack()
l.pack()

root.mainloop()
