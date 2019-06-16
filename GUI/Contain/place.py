from tkinter import *

win = Tk()

lbl1 = Label(win, text = 'text label', font = 'Times 30', bg = 'red')
lbl1.place(relwidth = '0.5', relheight = '1.0', x = 0, y = 0)

# lbl2 = Label(win, text = 'text label', font = 'Times 30', bg = 'green')
# lbl2.place(relwidth = '0.5', relheight = '1.0', relx = '0.1', rely = '0.3')

win.mainloop()