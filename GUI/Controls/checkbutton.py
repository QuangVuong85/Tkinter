from tkinter import *


master = Tk()

master.geometry("200x100")

lblframe = LabelFrame(master, text="Age")
lblframe.pack(side=TOP, fill=X)

checkbutton1 = Checkbutton(lblframe, text="Duoi 18")
checkbutton1.pack()

checkbutton2 = Checkbutton(lblframe, text="Duoi 30")
checkbutton2.pack()

master.mainloop()