from tkinter import *

root = Tk()

for row in range(3):
    root.columnconfigure(row, weight=1, minsize=50)
    root.rowconfigure(row, weight=1, minsize=50)
    for column in range(3):
        frame = Frame(
            root,
            relief=RAISED,
            borderwidth=5
        )
        frame.grid(row=row, column=column, padx=10, pady=10)
        label = Label(frame, text=f'Row: {row},\nColumn: {column}')
        label.pack(padx=10, pady=10)

root.mainloop()
