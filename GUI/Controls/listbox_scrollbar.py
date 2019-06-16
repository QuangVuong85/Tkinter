from tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

lsBox = Listbox(master, bg="Blue", fg="White", selectbackground="Red",
                highlightcolor="Yellow", font=20, yscrollcommand=scrollbar.set)
lsBox.pack(side=LEFT, fill=BOTH)

for line in range(1000):
    lsBox.insert(END, "This is line number " + str(line))

master.mainloop()
