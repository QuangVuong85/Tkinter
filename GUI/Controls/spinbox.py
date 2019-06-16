from tkinter import *


master = Tk()

spinboxDay = Spinbox(master, font=12, fg="Blue", from_=1, to=31)
spinboxDay.pack(side=LEFT)

spinboxMonth = Spinbox(master, font=12, fg="Green", value=("Jan", "Feb",
                                                           "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                                                           "Sep", "Oct", "Nov", "Dec"))
spinboxMonth.pack(side=LEFT)

spinboxYear = Spinbox(master, font=12, fg="Red", from_=1900, to=2100)
spinboxYear.pack(side=LEFT)

master.mainloop()
