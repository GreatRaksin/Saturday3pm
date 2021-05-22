from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from datetime import datetime
import platform
try:
    import winsound  # для windows
except:
    import os  # для остальных систем


def clock():
    date_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S/%p')
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minute, second = time2.split(':')
    if 12 < int(hour) < 24:  # если 16:23:44, сделать
        time = f'{str(int(hour) - 12)}:{minute}:{second} {time3}'
        # 04:23:44 PM
    else:
        time = f'{time2} {time3}'  # 02:55:13 PM
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)


def alarm():
    main_time = datetime.now().strftime('%H:%M %p')
    alarm_time = get_alarm_time_entry.get()
    alarm_time1, alarm_time2 = alarm_time.split()
    alarm_hour, alarm_minute = alarm_time1.split(':')
    main_time1, main_time2 = main_time.split()
    main_hour, main_minute = main_time1.split(':')
    if 12 < int(main_hour) < 24:
        main_hour = f'{str(int(main_hour) - 12)}'
    else:
        main_hour = alarm_hour
    if int(alarm_hour) == int(main_hour) and int(alarm_minute) == int(main_minute):
        for i in range(3):
            alarm_status.config(text='Пора вставать!')
            if platform.system() == 'Windows':
                winsound.Beep(5000, 1000)
            elif platform.system() == 'Darwin':
                os.system('say Time is up')
                print('Вставай')
            elif platform.system() == 'Linux':
                os.system('beep -f 5000')

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


# Делаем часы
time_label = Label(clock_tab, font='calibri 40 bold',
                   foreground='#54ff9f', background='black')
# ^ привязываю лейбл к вкладке, настраиваю шрифт (40пт, жирный), указываю цвет текста, цвет фона
time_label.pack(anchor='center')  # упаковать с привязкой к центру
date_label = Label(clock_tab, font='calibri 40 bold',
                   foreground='#54ff9f', background='black')
date_label.pack(anchor='s')  # опускался вниз


# делаем будильник
get_alarm_time_entry = Entry(alarm_tab, font='calibri 15 bold')  # поле для ввода времени, когда вас нужно разбудить
get_alarm_time_entry.pack(anchor='center')
alarm_label = Label(alarm_tab, font='calibri 20 bold',
                    text='Укажите время подъема в формате:\n07:30 AM\nЧасы: 07, Минуты: 30')
alarm_label.pack(anchor='s')
alarm_btn = Button(alarm_tab, text='Завести будильник!', command=alarm)
alarm_btn.pack(anchor='s')
alarm_status = Label(alarm_tab, font='calibri 15 bold')
alarm_status.pack(anchor='s')

if __name__ == "__main__":
    clock()
    root.mainloop()
