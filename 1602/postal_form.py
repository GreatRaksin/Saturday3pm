from tkinter import *

root = Tk()
root.title('Address entry form')

frameForm = Frame(relief=GROOVE, borderwidth=3)
frameForm.pack()

labels = [
    'First Name: ',
    'Last Name: ',
    'Address line 1: ',
    'Address line 2: ',
    'City: ',
    'State/province: ',
    'Postal code: ',
    'Country: '
]

for idx, text in enumerate(labels):
    label = Label(frameForm, text=text)
    entry = Entry(frameForm, width=50)

    label.grid(row=idx, column=0)
    entry.grid(row=idx, column=1)

frameButtons = Frame()
frameButtons.pack(ipadx=5, ipady=5)

btn_submit = Button(frameButtons, text='Submit')
btn_clear = Button(frameButtons, text='Clear')
btn_submit.pack(side=RIGHT, padx=10, ipady=10)
btn_clear.pack(side=RIGHT, padx=10, ipady=10)

root.mainloop()
