from tkinter import *
from tkinter import messagebox


def printxy():
    messagebox.showinfo('Message', "Click")


def callbackGet():
    print(var.get())


def callbackSet():
    var.set("")


win = Tk()

# Entry field set the entry text in a variable
var = StringVar()

# Matrix Button
for i in range(5):
    for j in range(5):
        Button(win, text='(%d, %d)' % (i, j), bg='#0fff0f',
               font='Times 20', borderwidth=10, command=printxy).grid(column=j, row=i)

### rowspan, columnspan
frame = Frame(win, bg='red')
frame.grid(row=6, columnspan=6, sticky=W+E)
btnGet = Button(frame, text="GET", command=callbackGet)
btnGet.pack(side=LEFT)
btnClear = Button(frame, text="CLEAR", command=callbackSet)
btnClear.pack(side=RIGHT)

entry = Entry(win, textvariable=var, font=20)
entry.grid(row=7, columnspan=7, sticky=W+E)

win.config(bg="#0fff0f")
win.mainloop()
