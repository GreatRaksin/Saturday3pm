from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from datetime import datetime
import platform
try:
    import winsound  # для windows
except:
    import os  # для остальных систем


root = Tk()
root.title('Digital clock')  # название приложения (отображается в окошке наверху)
root.geometry('500x250')  # размер окна

tabs_control = Notebook(root)  # создаю вкладки
clock_tab = Frame(tabs_control)  # вкладка для часов
alarm_tab = Frame(tabs_control)  # вкладка для будильника
stopwatch_tab = Frame(tabs_control)  # вкладка для секундомера
timer_tab = Frame(tabs_control)  # вкладка для таймера

tabs_control.add(clock_tab, text='Часы')
tabs_control.add(alarm_tab, text='Будильник')
tabs_control.add(stopwatch_tab, text='Секундомер')
tabs_control.add(timer_tab, text='Таймер')
tabs_control.pack(expand=1, fill='both')


if __name__ == "__main__":
    root.mainloop()