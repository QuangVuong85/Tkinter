from tkinter import *
from tkinter import messagebox
import random as rd

def random_value():
    messagebox.showinfo("Message", "Value random=%f"%rd.random())

master = Tk()
master.title("Title")

lableframe = LabelFrame(master, fg="red", font=14, text="Random value")
lableframe.place(relwidth = '1.0', relheight = '0.3')

btn = Button(lableframe, text = "Click here", fg = "blue", command=random_value)
btn.pack(side=BOTTOM)
lbl = Label(lableframe, text="Lable Test LableFrame", font=30)
lbl.pack(side=BOTTOM)


master.mainloop()