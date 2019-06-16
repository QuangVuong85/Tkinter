from tkinter import *


def select():
    sel = "Value="+str(var.get())
    lbl.config(text=sel)


master = Tk()

var = DoubleVar()

scale = Scale(master, variable=var, from_=0, to=100, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

btn = Button(master, text="Value", command=select)
btn.pack(anchor=CENTER)

lbl = Label(master)
lbl.pack(anchor=CENTER)

master.mainloop()
