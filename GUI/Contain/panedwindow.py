from tkinter import *

#default: orient=HORIZONTAL
master = PanedWindow()

master.pack(fill=BOTH, expand=5)

txt = Text(master, bd=1)
master.add(txt)

w2 = PanedWindow(master, orient=VERTICAL)
master.add(w2)

txt1 = Text(w2)
txt2 = Text(w2)
w2.add(txt1)
w2.add(txt2)

btn = Button(w2, text="ADD")
w2.add(btn)

master.config(bg="#0fff00")
master.mainloop()