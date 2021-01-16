from tkinter import *

borders = {
   'flat': FLAT,
   'sunken': SUNKEN,
   'raiser': RAISED,
    'groove': GROOVE,
    'ridge': RIDGE
}

root = Tk()
frame_a = Frame()
frame_b = Frame()

label_a = Label(master=frame_a, text='I am frame A')
label_b = Label(master=frame_b, text='I am frame B')
label_a.pack()
label_b.pack()


frame_b.pack()
frame_a.pack()

for border_name, relief in borders.items():
    frame = Frame(master=root, relief=relief, borderwidth=5)
    frame.pack(side=LEFT)

    label = Label(master=frame, text=border_name)
    label.pack()

root.mainloop()