from tkinter import *

def btnrelease(click):
    lbl = Label(frame1, text="Blue", fg="Blue")
    lbl.pack(side=TOP)

master = Tk()

master.geometry("400x300")

frame1=Frame(master, width=200, height=150, bg="Blue")
frame1.bind("<ButtonRelease>", btnrelease)
frame1.grid(row=0, column=0)

frame2=Frame(master, width=200, height=150, bg="Red")
frame2.grid(row=1, column=0)

frame3=Frame(master, width=200, height=150, bg="Green")
frame3.grid(row=0, column=1)

frame4=Frame(master, width=200, height=150, bg="Yellow")
frame4.grid(row=1, column=1)

master.mainloop()