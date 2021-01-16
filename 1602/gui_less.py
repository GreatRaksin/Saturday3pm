from tkinter import *

root = Tk()
textBox = Text(root)
textBox.pack()

lab = Label(root)
lab.pack()

btn = Button(root, text='Получить')
btn.pack()


def getting_text(event):
    res = textBox.get('1.0', '1.5')
    textBox.delete('1.0', END)
    lab['text'] = res


btn.bind('<Button-1>', getting_text)
root.mainloop()
