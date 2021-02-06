from tkinter import *

root = Tk()
frame = Frame(master=root, width=150, height=100)
frame.pack()

label1 = Label(frame, text='I am at (10, 10)', bg='#f5d3ee')
label1.place(x=10, y=10)

label2 = Label(frame, text='I am at (50, 75)', bg='#ff4df2')
label2.place(x=50, y=75)
root.mainloop()